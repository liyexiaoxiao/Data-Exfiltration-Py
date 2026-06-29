import os
import itertools
import pandas as pd

from statsmodels.stats.contingency_tables import cochrans_q, mcnemar
from statsmodels.stats.multitest import multipletests


INPUT_FILES = [
    r"D:\大创\support_materials\RQ5\statistic test\benchA_1.xlsx",
    r"D:\大创\support_materials\RQ5\statistic test\benchA_3.xlsx",
    r"D:\大创\support_materials\RQ5\statistic test\benchA_10.xlsx",
    r"D:\大创\support_materials\RQ5\statistic test\benchB_1.xlsx",
    r"D:\大创\support_materials\RQ5\statistic test\benchB_3.xlsx",
    r"D:\大创\support_materials\RQ5\statistic test\benchB_10.xlsx",
]
TOOLS = ["cerebro", "hybrid", "cuckoo", "virustotal", "EA4MP"]

Y_TRUE_COL = "y_ture"  
PACKAGE_COL = "package"

# 输出目录
OUT_DIR = r"D:\大创\support_materials\RQ5\statistic test\stats_outputs"
# ===================================

def safe_crosstab(a: pd.Series, b: pd.Series) -> pd.DataFrame:
    tab = pd.crosstab(a, b)
    for i in [0, 1]:
        if i not in tab.index:
            tab.loc[i] = 0
        if i not in tab.columns:
            tab[i] = 0
    tab = tab.sort_index().sort_index(axis=1)
    return tab


def compute_correct_matrix(df: pd.DataFrame, tools: list, y_col: str) -> pd.DataFrame:
    correct = pd.DataFrame(index=df.index)
    for t in tools:
        correct[f"correct_{t}"] = (df[t] == df[y_col]).astype(int)
    return correct


def run_cochrans_q(correct_df: pd.DataFrame):
    """
    兼容 statsmodels 不同版本：
    - 有的返回 (statistic, pvalue)
    - 有的返回 Bunch(statistic=..., pvalue=...)
    """
    cq = cochrans_q(correct_df.to_numpy())

    if isinstance(cq, tuple) and len(cq) >= 2:
        return float(cq[0]), float(cq[1])

    q_stat = getattr(cq, "statistic", None)
    q_p = getattr(cq, "pvalue", None)

    # 某些实现可能用 q/p 命名
    if q_stat is None:
        q_stat = getattr(cq, "q", None)
    if q_p is None:
        q_p = getattr(cq, "p", None)

    if q_stat is None or q_p is None:
        raise RuntimeError(f"Unexpected cochrans_q return type: {type(cq)}")

    return float(q_stat), float(q_p)


def run_stats_for_file(path: str) -> dict:
    df = pd.read_excel(path)

    missing = [c for c in [PACKAGE_COL, Y_TRUE_COL] + TOOLS if c not in df.columns]
    if missing:
        raise ValueError(f"[{os.path.basename(path)}] 缺少列: {missing}")

    for c in [Y_TRUE_COL] + TOOLS:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    before = len(df)
    df = df.dropna(subset=[Y_TRUE_COL] + TOOLS).copy()
    after = len(df)

    df[Y_TRUE_COL] = df[Y_TRUE_COL].astype(int)
    for t in TOOLS:
        df[t] = df[t].astype(int)

    correct = compute_correct_matrix(df, TOOLS, Y_TRUE_COL)

    # Cochran's Q（修复点在这里）
    q_stat, q_p = run_cochrans_q(correct)

    # Pairwise McNemar
    pairs = []
    for t1, t2 in itertools.combinations(correct.columns.tolist(), 2):
        tab = safe_crosstab(correct[t1], correct[t2])

        b = tab.loc[1, 0]
        c = tab.loc[0, 1]
        if (b + c) == 0:
            p = 1.0
            note = "identical outcomes (b+c=0)"
        else:
            res = mcnemar(tab, exact=True)
            p = float(res.pvalue)
            note = ""

        pairs.append({
            "tool1": t1.replace("correct_", ""),
            "tool2": t2.replace("correct_", ""),
            "b(1,0)": int(b),
            "c(0,1)": int(c),
            "p_value": p,
            "note": note
        })

    pairwise_df = pd.DataFrame(pairs)

    reject, p_corr, _, _ = multipletests(
        pairwise_df["p_value"].values,
        alpha=0.05,
        method="holm"
    )
    pairwise_df["p_holm"] = p_corr
    pairwise_df["significant_0.05"] = reject

    summary = {
        "file": os.path.basename(path),
        "n_rows_raw": before,
        "n_rows_used": after,
        "n_rows_dropped_na": before - after,
        "cochran_Q": float(q_stat),
        "cochran_p": float(q_p),
        "cochran_significant_0.05": bool(q_p < 0.05),
    }

    return {"summary": summary, "pairwise": pairwise_df}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    all_summaries = []
    all_pairwise = []

    for f in INPUT_FILES:
        print("=" * 80)
        print(f"Processing: {f}")

        result = run_stats_for_file(f)
        summary = result["summary"]
        pairwise = result["pairwise"]

        all_summaries.append(summary)

        bench_name = os.path.splitext(os.path.basename(f))[0]
        pairwise.insert(0, "benchmark", bench_name)
        all_pairwise.append(pairwise)

        out_xlsx = os.path.join(OUT_DIR, f"{bench_name}_stats.xlsx")
        with pd.ExcelWriter(out_xlsx, engine="openpyxl") as writer:
            pd.DataFrame([summary]).to_excel(writer, index=False, sheet_name="summary")
            pairwise.to_excel(writer, index=False, sheet_name="pairwise_mcnemar")

        print(f"[DONE] Cochran Q={summary['cochran_Q']:.4f}, p={summary['cochran_p']:.4g}, "
              f"used_rows={summary['n_rows_used']} (dropped_na={summary['n_rows_dropped_na']})")
        print(f"Saved: {out_xlsx}")

    summary_df = pd.DataFrame(all_summaries)
    pairwise_all_df = pd.concat(all_pairwise, ignore_index=True)

    out_all = os.path.join(OUT_DIR, "ALL_benchmarks_stats.xlsx")
    with pd.ExcelWriter(out_all, engine="openpyxl") as writer:
        summary_df.to_excel(writer, index=False, sheet_name="all_summary")
        pairwise_all_df.to_excel(writer, index=False, sheet_name="all_pairwise_mcnemar")

    print("=" * 80)
    print("ALL DONE")
    print(f"Combined results saved to: {out_all}")


if __name__ == "__main__":
    main()
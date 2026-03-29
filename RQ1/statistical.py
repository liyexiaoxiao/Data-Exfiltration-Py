import pymannkendall as mk
from scipy.stats import spearmanr
import numpy as np
# download count（2017-2024）
malware = [1771, 682, 11, 1, 2072, 1932, 4489, 3045]
data_exfiltration = [771, 1314, 1132, 1427, 4348, 11976, 2851, 4417]

# Mann-Kendall test
result_malware = mk.original_test(malware)
result_exfil = mk.original_test(data_exfiltration)

print("===== Malware Packages =====")
print(result_malware)

print("\n===== Data Exfiltration Packages =====")
print(result_exfil)

from statsmodels.stats.proportion import proportions_ztest

count = 58
nobs = 83
value = 0.5  # 对比 50%

stat, p = proportions_ztest(count, nobs, value)
print("z =", stat)
print("p =", p)

# years
years = np.arange(2017, 2025)

# benign downloads
benign_downloads = np.array([
    4032211,
    6824261,
    10069119,
    20440191,
    13371524,
    41976766,
    170219728,
    811167297
])

# Spearman correlation
rho, p_value = spearmanr(years, benign_downloads)

print("Spearman rho:", rho)
print("p-value:", p_value)
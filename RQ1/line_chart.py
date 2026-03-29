# import matplotlib.pyplot as plt
# import os

# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size'] = 14

# # year and download counts
# years = list(range(2017, 2025))
# malware_counts = [590, 227, 4, 1, 0, 617, 6980, 1766]       # 蓝色线：Malware
# data_exfil_counts = [771, 1314, 1132, 1427, 4348, 11976, 2851, 4417]      # 红色线：Data Exfiltration

# # figure
# plt.figure(figsize=(10, 5))
# plt.plot(years, malware_counts, marker='o', color='#0000CC', linestyle='-', linewidth=2, label='Malware')
# plt.plot(years, data_exfil_counts, marker='o', color='#CC0000', linestyle='-', linewidth=2, label='Data Exfiltration')

# # label
# plt.xlabel("Year")
# plt.ylabel("Download Count")

# plt.xticks(years)
# plt.yticks()
# plt.grid(True, linestyle='--', alpha=0.5)

# # The red line value is displayed above the point, the blue line value is displayed below the point, and the exception 6980 is displayed above the point
# for x, y in zip(years, malware_counts):
#     if y == 6980:
#         plt.text(x, y + 80, str(y), ha='center', va='bottom', color='black')
#     else:
#         plt.text(x, y - 150, str(y), ha='center', va='top', color='black')

# for x, y in zip(years, data_exfil_counts):
#     if y == 2851:
#         plt.text(x, y - 150, str(y), ha='center', va='top', color='black')
#     else:
#         plt.text(x, y + 80, str(y), ha='center', va='bottom', color='black')

# plt.legend()

# plt.tight_layout()

# # sav as PDF
# desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "download_counts.pdf")
# plt.savefig(desktop_path, format='pdf')

# # show the fig
# plt.show()
#-------------------------------------------------------------------------------------------------
# import matplotlib.pyplot as plt
# import os

# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size'] = 12

# years = list(range(2017, 2025))

# # =========================
# # total downloads
# # =========================
# malware_total_downloads = [1771, 682, 11, 1, 2072, 1932, 4489, 3045]
# data_exfil_total_downloads = [771, 1314, 1132, 1427, 4348, 11976, 2851, 4417]
# benign_total_downloads = [4032211, 6824261, 10069119, 20440191, 13371524, 41976766, 170219728, 811167297]

# # =========================
# # package counts
# # =========================
# malware_package_counts = [1, 2, 3, 3, 3, 18, 73, 83]
# data_exfil_package_counts = [1, 2, 3, 3, 3, 62, 73, 83]
# benign_package_counts = [1, 2, 3, 3, 3, 62, 73, 83]

# # =========================
# # compute averages
# # =========================
# def compute_avg_downloads(total_downloads, package_counts):
#     avg = []
#     for total, count in zip(total_downloads, package_counts):
#         avg.append(total / count if count else 0)
#     return avg

# malware_avg = compute_avg_downloads(malware_total_downloads, malware_package_counts)
# data_exfil_avg = compute_avg_downloads(data_exfil_total_downloads, data_exfil_package_counts)
# benign_avg = compute_avg_downloads(benign_total_downloads, benign_package_counts)

# # =========================
# # plot
# # =========================
# plt.figure(figsize=(11, 5))

# plt.plot(years, malware_avg, marker='o', color='#0000CC', linewidth=2, label='Malware')
# plt.plot(years, data_exfil_avg, marker='o', color='#CC0000', linewidth=2, label='Data Exfiltration')
# plt.plot(years, benign_avg, marker='o', color='#008000', linewidth=2, label='Benign')

# plt.yscale('log')

# plt.xlabel("Year")
# plt.ylabel("Average Downloads per Package (log scale)")
# plt.xticks(years)

# plt.grid(True, which='both', linestyle='--', alpha=0.5)

# # =========================
# # annotate numbers (上下标注，不左右偏移)
# # =========================
# label_fontsize = 14

# # Malware：标在点下方
# for x, y in zip(years, malware_avg):
#     plt.text(x, y * 0.82, f"{y:.1f}", fontsize=label_fontsize,
#              ha='center', va='top', color='black')

# # Data Exfiltration：标在点上方
# for x, y in zip(years, data_exfil_avg):
#     plt.text(x, y * 1.15, f"{y:.1f}", fontsize=label_fontsize,
#              ha='center', va='bottom', color='black')

# # Benign：标在点上方，更高一点
# for x, y in zip(years, benign_avg):
#     plt.text(x, y * 1.08, f"{y:.1f}", fontsize=label_fontsize,
#              ha='center', va='bottom', color='black')

# # legend 右上角但下移，避免挡线
# plt.legend(loc='upper right', bbox_to_anchor=(1.0, 0.85))

# plt.tight_layout()

# desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "avg_downloads_per_package_log.pdf")
# plt.savefig(desktop_path, format='pdf', bbox_inches='tight')

# plt.show()
#-------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator
import os

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14

years = list(range(2017, 2025))

# =========================
# total downloads
# =========================
malware_downloads = [1771, 682, 11, 1, 2072, 1932, 4489, 3045]
data_exfil_downloads = [771, 1314, 1132, 1427, 4348, 11976, 2851, 4417]
benign_downloads = [4032211, 6824261, 10069119, 20440191, 13371524, 41976766, 170219728, 811167297]

# =========================
# plot
# =========================
plt.figure(figsize=(11, 5))

plt.plot(years, malware_downloads, marker='o', color='#0000CC', linewidth=2, label='Malware')
plt.plot(years, data_exfil_downloads, marker='o', color='#CC0000', linewidth=2, label='Data Exfiltration')
plt.plot(years, benign_downloads, marker='o', color='#008000', linewidth=2, label='Benign')

plt.yscale('log')
ax = plt.gca()
ax.yaxis.set_major_locator(LogLocator(base=10, numticks=12))

plt.xlabel("Year")
plt.ylabel("Downloads (log scale)")
plt.xticks(years)

plt.grid(True, which='both', linestyle='--', alpha=0.5)

# =========================
# annotate numbers
# =========================
label_fontsize = 14

# Malware
for x, y in zip(years, malware_downloads):

    if x == 2017 or x == 2023:
        plt.text(x, y * 1.25, f"{y}", fontsize=label_fontsize,
                 ha='center', va='bottom')

    elif x == 2021:
        plt.text(x + 0.12, y * 0.85, f"{y}", fontsize=label_fontsize,
                 ha='left', va='top')

    elif x == 2018:
        plt.text(x - 0.12, y * 0.85, f"{y}", fontsize=label_fontsize,
                 ha='right', va='top')

    else:
        plt.text(x, y * 0.75, f"{y}", fontsize=label_fontsize,
                 ha='center', va='top')


# Data Exfiltration
for x, y in zip(years, data_exfil_downloads):

    if x == 2017 or x == 2023:
        plt.text(x, y * 0.75, f"{y}", fontsize=label_fontsize,
                 ha='center', va='top')

    else:
        plt.text(x, y * 1.25, f"{y}", fontsize=label_fontsize,
                 ha='center', va='bottom')


# Benign
for x, y in zip(years, benign_downloads):
    plt.text(x, y * 1.05, f"{y}", fontsize=label_fontsize,
             ha='center', va='bottom')


# legend
plt.legend(loc='upper right', bbox_to_anchor=(1.0, 0.85))

plt.tight_layout()

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "downloads_log.pdf")
plt.savefig(desktop_path, format='pdf', bbox_inches='tight')

plt.show()
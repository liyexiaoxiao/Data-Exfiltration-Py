import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 14

# year and download counts
years = list(range(2017, 2025))
malware_counts = [590, 227, 4, 1, 0, 617, 6980, 1766]       # 蓝色线：Malware
data_exfil_counts = [771, 1314, 1132, 1427, 4348, 11976, 2851, 4417]      # 红色线：Data Exfiltration

# figure
plt.figure(figsize=(10, 5))
plt.plot(years, malware_counts, marker='o', color='#0000CC', linestyle='-', linewidth=2, label='Malware')
plt.plot(years, data_exfil_counts, marker='o', color='#CC0000', linestyle='-', linewidth=2, label='Data Exfiltration')

# label
plt.xlabel("Year")
plt.ylabel("Download Count")

plt.xticks(years)
plt.yticks()
plt.grid(True, linestyle='--', alpha=0.5)

# The red line value is displayed above the point, the blue line value is displayed below the point, and the exception 6980 is displayed above the point
for x, y in zip(years, malware_counts):
    if y == 6980:
        plt.text(x, y + 80, str(y), ha='center', va='bottom', color='black')
    else:
        plt.text(x, y - 150, str(y), ha='center', va='top', color='black')

for x, y in zip(years, data_exfil_counts):
    if y == 2851:
        plt.text(x, y - 150, str(y), ha='center', va='top', color='black')
    else:
        plt.text(x, y + 80, str(y), ha='center', va='bottom', color='black')

plt.legend()

plt.tight_layout()

# sav as PDF
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "download_counts.pdf")
plt.savefig(desktop_path, format='pdf')

# show the fig
plt.show()

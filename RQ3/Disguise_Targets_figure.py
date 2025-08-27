import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.ticker import PercentFormatter

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 28

# X
patterns = ['Download Process', 'Operation Process', 'Stolen Information', 
            'Remote Address', 'Composite Targets', 'None']

# percentages data
percentages = [69.8, 8.4, 7.2, 1.2, 6.0, 7.4]

fig, ax = plt.subplots(figsize=(18, 10))

bar_width = 0.3 * 1/3 
x_spacing = 0.16        
x = np.arange(len(patterns)) * x_spacing

# fig
bars = ax.bar(x, percentages, width=bar_width, color='#0000CC', label='Targets Distribution')

# label
ax.set_xlabel('Disguise Targets')
ax.set_ylabel('Percentage')

ax.set_xticks(x)
ax.set_xticklabels(patterns, rotation=45)
ax.tick_params(axis='y')

ax.yaxis.set_major_formatter(PercentFormatter(xmax=100))

ax.bar_label(bars, labels=[f"{v:.1f}%" for v in percentages], padding=5)

ax.set_ylim(0, 80)

plt.tight_layout()

# save fig
plt.savefig(r'C:\Users\uu\Desktop\targets_distribution.pdf')
plt.show()

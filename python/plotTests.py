import matplotlib
import matplotlib.pyplot as plt
import numpy as np


men_means, men_std = (20, 35, 30, 35, 27), (2, 3, 4, 1, 2)
women_means, women_std = (25, 32, 34, 20, 25), (3, 5, 2, 3, 3)
undef_means, undef_std = (25, 32, 34, 20, 25), (3, 5, 2, 3, 3)
ind = np.arange(len(men_means))  # the x locations for the groups
width = 1  # the width of the bars

fig, ax = plt.subplots()
ax.bar(6*ind - 1, men_means, width, yerr=men_std,
                label='Men')
ax.bar(6*ind - 2, women_means, width, yerr=women_std,
                label='Women')
ax.bar(6*ind - 3, undef_means, width, yerr=undef_std,
                label='undef')                

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')

ax.set_xticks(6*ind-3)
#ax.set_xticks(ind)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))


ax.legend()




fig.tight_layout()

plt.show()




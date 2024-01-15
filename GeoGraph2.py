import matplotlib.pyplot as plt
import numpy as np
from math import comb

plt.style.use('_mpl-gallery')

fig, ax = plt.subplots()

ax.set(xlim=(0, 7), xticks=np.arange(0, 8),
       ylim=(0, 1), yticks=np.arange(0, 1, step = 0.1))

plt.subplots_adjust(left=0.15,bottom=0.15,right=0.95,top=0.95, wspace=0.2, hspace=0.2)

card_range = list(range(28, 43))

for count in card_range:
    x = list(range(0, 8))
    y = list(range(0, 8))

    population = 99
    sample = 7
    sucesses = count


    for i in range(8):
        y[i] = comb(sucesses, i) * comb(population - sucesses, sample - i) / comb(population, sample)

    ax.plot(x, y, linewidth=2.0)

plt.show()



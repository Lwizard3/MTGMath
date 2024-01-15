import matplotlib.pyplot as plt
import numpy as np
from math import comb

plt.style.use('_mpl-gallery')

num_cards = 99
num_target = 99
opening_x = 11
needed = 1

def hypergeo(population, sucesses, sample, at_least):
    prob = 0
    for count in range(at_least, sample + 1):
        prob += comb(sucesses, count) * comb(population - sucesses, sample - count) / comb(population, sample)

    return prob


# plot
fig, ax = plt.subplots()

ax.set(xlim=(0, opening_x), xticks=np.arange(0, opening_x + 1),
       ylim=(0, 1), yticks=np.arange(0, 1, step = 0.1))

plt.subplots_adjust(left=0.15,bottom=0.15,right=0.95,top=0.95, wspace=0.2, hspace=0.2)

for sample in range(1, num_target + 1):
    x = list(range(0, opening_x + 1))
    y = list(range(0, opening_x + 1))

    for i in range(opening_x + 1):
        y[i] = hypergeo(num_cards, x[i], sample, needed)
        
    ax.plot(x, y, linewidth=2.0)





plt.show()
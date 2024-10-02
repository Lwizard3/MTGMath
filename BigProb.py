import math
import matplotlib.pyplot as plt
from math import comb

def Hypergeometric(population, pop_sucesses, sample, sample_sucesses):
    return comb(pop_sucesses, sample_sucesses) * comb(population - pop_sucesses, sample - sample_sucesses) / comb(population, sample)

def AtLeastHypergeometric(population, pop_sucesses, sample, sample_sucesses):
    prob = 0
    for value in range(sample_sucesses, sample + 1):
        prob += comb(pop_sucesses, value) * comb(population - pop_sucesses, sample - value) / comb(population, sample)

Population = 99
Pop_sucesses = 37
Sample = 7
Sample_sucesses = 3


def Mulligan(max_mull_size):
    prob = Hypergeometric(Population, Pop_sucesses, 7, Sample_sucesses)
    print(prob)
    for hand_size in range(7, max(max_mull_size - 1, Sample_sucesses), -1):
        block_prob = 1 - prob
        mull_prob = Hypergeometric(Population, Pop_sucesses, 7, Sample_sucesses) * block_prob
        prob += mull_prob
        print(prob)

    return prob

Population = 99
Pop_sucesses_table = [1, 17]
Sample = 7
Sample_sucesses_table = [1, 3]

def Multivariate_Intersect(population, pop_sucesses_table, sample, sample_sucesses_table):
    prob = 1
    pop_sucesses_table.append(population - sum(pop_sucesses_table))
    sample_sucesses_table.append(sample - sum(sample_sucesses_table))
    for i in range(len(pop_sucesses_table)):
        prob *= comb(pop_sucesses_table[i], sample_sucesses_table[i])
    prob /= comb(population, sample)

    return prob

print(Multivariate_Intersect(Population, Pop_sucesses_table, Sample, Sample_sucesses_table))

def At_Least_Multivariate_Intersect(population, pop_sucesses_table, sample, sample_sucesses_table):
    prob = 0
    for sucesss_1 in range(sample_sucesses_table[0], sample):
        for sucesss_2 in range(sample_sucesses_table[1], sample):
            for sucesss_3 in range(sample_sucesses_table[2], sample):
                if (sucesss_1 + sucesss_2 + sucesss_3 > sample):
                    continue
                prob += Multivariate_Intersect(Population, Pop_sucesses_table, Sample, [sucesss_1, sucesss_2, sucesss_3])
    return prob


print(At_Least_Multivariate_Intersect(Population, Pop_sucesses_table, Sample, Sample_sucesses_table))
import numpy as np

def swap_mutation(ordering, mutation_rate=0.2):
    new_ordering = ordering[:]

    if np.random.rand() < mutation_rate:
        i,j = np.random.choice(len(new_ordering), size=2, replace=False)
        new_ordering[i], new_ordering[j] = new_ordering[j], new_ordering[i]

    return new_ordering  
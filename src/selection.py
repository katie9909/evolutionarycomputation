import numpy as np

def tournament_selection(orderings, fitness_values, k=3):
    idxs = np.random.choice(len(orderings), size=k, replace=False)
    best_index = int(idxs[0])

    for j in idxs[1:]:
        j = int(j)
        if fitness_values[j] < fitness_values[best_index]:
            best_index = j

    return orderings[best_index]

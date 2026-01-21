import numpy as np

def ordered_crossover(parent1, parent2):
    n=len(parent1)
    child = [-1] * n

    start, end = np.random.choice(n, size=2, replace=False)
    if start > end:
        start, end = end, start
    
    for i in range(start, end + 1):
        child[i] = parent1[i]
    
    fill_pos = 0
    for gene in parent2:
        if gene not in child:
            while child[fill_pos] != -1:
                fill_pos += 1
            child[fill_pos] = gene

    return child
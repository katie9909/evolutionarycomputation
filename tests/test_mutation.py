import numpy as np
from mutation import swap_mutation

np.random.seed(1)

ordering = [0,1,2,3,4]
print("Before:", ordering)

for t in range(5):
    mutated = swap_mutation(ordering, mutation_rate=1.0)
    print("After: ", mutated)
    
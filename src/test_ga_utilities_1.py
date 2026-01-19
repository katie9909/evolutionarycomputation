import numpy as np
from container import Container
from ga_utilities import initialise_orderings, evaluate_population

np.random.seed(1)

container = Container(width=20, height=15, max_weight=500)
radii = [2,3,2.5,1.5,1.2]
weights = [10,10,10,10,10]

population = initialise_orderings(
    population_size = 5,
    n_cylinders = len(radii)
)

fitness_values = evaluate_population(container, radii, weights, population)

for i in range(len(population)):
    fit = fitness_values[i]
    print(f"Ordering {i}: {population[i]} fitness {fit:.2f}")


import numpy as np
from container import Container
from ga_utilities import initialise_orderings, evaluate_population 
from selection import tournament_selection

np.random.seed(1)

container = Container(width=20, height=15, max_weight=500)
radii = [2,3,2.5,1.5,1.2]
weights = [10, 10, 10, 10, 10]

orderings = initialise_orderings(population_size=10, n_cylinders=len(radii))
fitness_values = evaluate_population(container, radii, weights, orderings)

parent = tournament_selection(orderings, fitness_values, k=3)

print("Selected parent:", parent)
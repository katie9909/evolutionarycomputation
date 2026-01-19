import numpy as np
from circle import Circle
from placement import Placement
from fitness import FitnessEvaluator

def create_random_ordering(n_cylinders):
    return [int(x) for x in np.random.permutation(n_cylinders)]

def evaluate_ordering(container,radii,weights,ordering):
    circles = [Circle(r,w) for r,w in zip(radii, weights)]

    placement = Placement(circles, container)
    placement.place_from_chromosome(ordering)

    # temp debug
    positions = [(float(c.x), float(c.y)) for c in circles]
    print("ordering:", ordering)
    print("positions:", positions)

    fitness_evaluator = FitnessEvaluator(container)
    return fitness_evaluator.calculate_fitness(circles)

def initialise_orderings(population_size, n_cylinders):
    population = []
    for _ in range(population_size):
        population.append(create_random_ordering(n_cylinders))
    return population

def evaluate_population(container, radii, weights, population):
    fitness_values = []
    for ordering in population:
        fitness_values.append(
            evaluate_ordering(container, radii, weights, ordering)
        )
    return fitness_values
import numpy as np
from circle import Circle
from container import Container
from placement import Placement
from fitness import FitnessEvaluator

def random_search(container, radii, weights, n_evaluations=1000, seed=42):
    np.random.seed(seed)

    circles = [Circle(r,w) for r,w in zip(radii, weights)]
    placement = Placement(circles, container)
    fitness_evaluator = FitnessEvaluator(container)

    best_ordering = None
    best_fitness = float("inf")

    fitness_history = []
    best_fitness_history = []

    n_circles = len(circles)

    for i in range(n_evaluations):
        ordering = list(np.random.permutation(n_circles))

        placement.place_from_chromosome(ordering)

        fitness = fitness_evaluator.calculate_fitness(circles)

        fitness_history.append(fitness)

        if fitness < best_fitness:
            best_fitness = fitness
            best_ordering = ordering
        
        best_fitness_history.append(best_fitness)

    return best_ordering, best_fitness, fitness_history, best_fitness_history






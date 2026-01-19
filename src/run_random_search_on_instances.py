import numpy as np

from container_instances import create_basic_instances
from circle import Circle
from container import Container
from placement import Placement
from fitness import FitnessEvaluator

def random_search(container, circles, n_evaluations=2000, seed=42):
    np.random.seed(seed)

    placement = Placement(circles, container)
    fitness_evaluator = FitnessEvaluator(container)

    n_circles = len(circles)
    best_ordering = None
    best_fitness = float("inf")

    for _ in range(n_evaluations):
        ordering = list(np.random.permutation(n_circles))
        placement.place_from_chromosome(ordering)
        fitness = fitness_evaluator.calculate_fitness(circles)

        if fitness < best_fitness:
            best_fitness = fitness
            best_ordering = ordering
    
    return best_ordering, best_fitness

def run_basic_instances(n_evaluations=2000, seed=42):
    instances = create_basic_instances()

    for idx, inst in enumerate(instances):
        container = Container(
            width = inst.container.width,
            height = inst.container.depth,
            max_weight = inst.container.max_weight

        )

        circles = [
            Circle(radius=c.diameter / 2, weight=c.weight)
            for c in inst.cylinders
        ]

        best_ordering, best_fitness = random_search(
            container, circles, n_evaluations=n_evaluations, seed=seed
        )

        placed_count = sum(1 for c in circles if c.placed)

        print(f"Basic instance {idx}: placed {placed_count}/{len(circles)} best_fitness={best_fitness:.2f}")
        print(f"best_ordering={best_ordering}")
    
run_basic_instances(n_evaluations=2000, seed=42)
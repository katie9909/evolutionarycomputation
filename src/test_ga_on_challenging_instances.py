from container import Container
from container_instances import create_challenging_instances
from ga_run import run_ga

def run_challenging_instances_ga(pop_size=100, n_gens=1000, mutation_rate=0.01, seed=1 ):
    instances = create_challenging_instances()

    for idx, inst in enumerate(instances):
        container = Container(
            width=inst.container.width,
            height=inst.container.depth,
            max_weight=inst.container.max_weight
        )

        radii = [c.diameter / 2 for c in inst.cylinders]
        weights = [c.weight for c in inst.cylinders]

        best_sol, best_fit = run_ga(
            container, radii, weights,
            pop_size = pop_size,
            n_gens=n_gens,
            k=3,
            p_mut = mutation_rate,
            p_xover= 0.9,
            elitism = 2,
            seed = seed,
            target_fitness=0.0

        )

        print(f"challenging instance {idx+4}: best_fit: {best_fit:.2f}, best_sol={best_sol}")

run_challenging_instances_ga(pop_size=100, n_gens=1000, mutation_rate=0.2, seed=1)
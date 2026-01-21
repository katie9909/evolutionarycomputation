from container import Container
from circle import Circle
from container_instances import create_basic_instances
from ga_run import run_ga

def run_basic_instances_ga(pop_size=30, n_gens=300, mutation_rate=0.3, seed =1 ):
    instances = create_basic_instances()

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
            n_gens = n_gens,
            k=3,
            p_mut = mutation_rate, 
            elitism = 1,
            seed = seed,
            target_fitness = 0.0
        )

        print(f"Basic instance {idx}: best_fit = {best_fit:.2f} best_sol={best_sol}")

run_basic_instances_ga(pop_size=40, n_gens=500, mutation_rate=0.3, seed=1)
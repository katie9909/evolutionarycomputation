from container import Container
from container_instances import create_basic_instances, create_challenging_instances
from visualise import visualise_solution
from ga_run import run_ga

if __name__ == "__main__":

    basic = create_basic_instances()

    for i, inst in enumerate(basic):
        container = Container(inst.container.width, inst.container.depth, inst.container.max_weight)
        radii = [c.diameter / 2 for c in inst.cylinders]
        weights = [c.weight for c in inst.cylinders]

        solution, best_fit = run_ga(
            container, radii, weights,
            pop_size = 60,
            n_gens = 300,
            k = 3,
            p_mut = 0.01,
            p_xover = 0.9,
            elitism = 2,
            seed = 1,
            target_fitness = 0.0
        )

        visualise_solution (container, radii, weights, solution,
                           title = f"Basic instance {i+1} (fitness={best_fit:.2f})",
                           save_path = f"results/basic_instance{i+1}.png")
    
    
    challenging = create_challenging_instances()

    for j, inst in enumerate(challenging):
        instance_id = j + 4
        container = Container(inst.container.width, inst.container.depth, inst.container.max_weight)
        radii = [c.diameter / 2 for c in inst.cylinders]
        weights = [c.weight for c in inst.cylinders]

        solution, best_fit = run_ga(
            container, radii, weights,
            pop_size=100,
            n_gens=1000,
            k=3,
            p_mut=0.01,
            p_xover =0.9,
            elitism=2,
            seed=1,
            target_fitness=0.0
        )

        visualise_solution (container, radii, weights, solution,
                           title = f"Challenging instance {instance_id} (fitness={best_fit:.2f})",
                           save_path = f"results/challenging_instance_{instance_id}.png")
    
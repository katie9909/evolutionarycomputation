import numpy as np
from ga_utilities import initialise_orderings, evaluate_population, evaluate_ordering
from selection import tournament_selection
from mutation import swap_mutation
from crossover import ordered_crossover 

def run_ga(container, radii, weights,
           pop_size=30, n_gens=200,
           k=3, p_mut=0.02, p_xover = 0.9, elitism=1,
           seed=1,
           target_fitness = 0.0):
    np.random.seed(seed)

    n=len(radii)

    pop = initialise_orderings(population_size = pop_size, n_cylinders=n)
    fit = evaluate_population(container, radii, weights, pop)

    best_i = int(np.argmin(fit))
    best = fit[best_i]
    best_sol = pop[best_i][:]

    print("gen",0, "best", best)

    for gen in range(1, n_gens + 1):

        new_pop = []

        if elitism > 0:
            elite_idxs = list(np.argsort(fit))[:elitism]
            for ei in elite_idxs:
                new_pop.append(pop[int(ei)][:])

        while len(new_pop) < pop_size:
            p1 = tournament_selection(pop, fit, k=k)
            p2 = tournament_selection(pop, fit, k=k)

            if np.random.rand() < p_xover:
                child = ordered_crossover(p1,p2) 
            else:
                child = p1[:]

            child = swap_mutation(child, mutation_rate=p_mut)
            new_pop.append(child)
        
        pop = new_pop
        fit = evaluate_population(container, radii, weights, pop)

        gen_best_i = int(np.argmin(fit))
        if fit[gen_best_i] < best:
            best = fit[gen_best_i]
            best_sol = pop[gen_best_i][:]
        
        if gen % 10 == 0:
            print("gen", gen, "best", best)
        
        if best <= target_fitness:
            print("perfect at gen", gen)
            break

    return best_sol, best 
    
        



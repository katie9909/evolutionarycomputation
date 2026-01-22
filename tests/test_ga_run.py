from container import Container
from ga_run import run_ga 

container = Container(width=20, height=15, max_weight=500)
radii = [2,3,2.5,1.5,1.2]
weights = [10,10,10,10,10]

best_sol, best = run_ga(
    container, radii, weights,
    pop_size = 30, n_gens=100,
    k=3, p_mut=0.2,
    elitism = 1, seed=1
)

print("best_sol:",best_sol)
print("best:", best)

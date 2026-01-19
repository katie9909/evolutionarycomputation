from circle import Circle
from container import Container
from placement import Placement
from fitness import FitnessEvaluator

circles = [
    Circle(2,10),
    Circle(3,10),
    Circle(2.5,10),
]

container = Container(width=20, height=15, max_weight= 500)

placement = Placement(circles,container)
placement.place_from_chromosome([0,1,2])

fe = FitnessEvaluator(container)

placed = [c for c in circles if c.placed]
print("Placed:", len(placed), "/", len(circles))
print("Positions:", [(float(c.x), float(c.y)) for c in circles])

print("Fitness:", fe.calculate_fitness(circles))


from circle import Circle
from container import Container
from placement import Placement
from fitness import FitnessEvaluator

container = Container(width=20, height=15, max_weight=500)

circles = [
    Circle(radius=2, weight=10),
    Circle(radius=3, weight=10),
    Circle(radius=2.5, weight=10)
]

placement = Placement(circles, container)
placement.place_from_chromosome([0,1,2])

fe = FitnessEvaluator(container)

print("calculate_fitness:", fe.calculate_fitness(circles))
print("debug_fitness:", fe.debug_fitness(circles))
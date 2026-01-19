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

print("Fitness:", fe.calculate_fitness(circles))


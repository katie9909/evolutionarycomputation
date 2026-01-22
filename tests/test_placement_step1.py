from circle import Circle
from container import Container
from placement import Placement 

circles = [
    Circle(radius=2, weight=10),
    Circle(radius=3, weight =10)
]

container = Container(width=20, height = 15, max_weight =500)

p = Placement(circles, container)
chromosome = [0,1]

p.place_from_chromosome(chromosome)

for i,c in enumerate(circles):
    print(i, "placed:", c.placed, "pos:", (float(c.x), float(c.y)))

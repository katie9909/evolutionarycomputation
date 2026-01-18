from circle import Circle
from container import Container

container = Container(width=20, height=15, max_weight=500)

c = Circle(radius=2, weight=10)
c.set_position(2,2)
print("inside should be true:", c.within_bounds(container))

c.set_position(1,1)
print("outside should be true:", c.within_bounds(container))


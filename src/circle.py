import numpy as np

class Circle:
    def __init__(self, radius, weight=1.0):
        self.radius = radius
        self.weight = weight 
        self.x = 0
        self.y = 0
        self.placed = False
    
    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.placed = True
    
    def distance_to(self,other):
        # calculate distance between centers of this circle and another
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def overlaps(self,other):
        # check if this circle overlaps with another circle
        distance = self.distance_to(other)
        return distance < (self.radius + other.radius - 0.01)
    
    def __str__(self):
        return f"Circle(r={self.radius:.1f}, w={self.weight:.1f}, pos=({self.x:.1f}, {self.y:.1f}))"


import numpy as np

class Placement:
    def __init__(self, circles, container):
        self.circles = circles
        self.container = container

    def reset(self):
        for c in self.circles:
            c.x = 0
            c.y = 0
            c.placed = False

    def place_from_chromosome(self,chromosome):
        self.reset()

        for idx in chromosome:
            circle = self.circles[idx]
            open_points = self.find_open_points(circle)

            if open_points:
                best = min(open_points, key=lambda p: p[2])
                circle.set_position(best[0], best[1])
        
        
    def find_open_points(self, new_circle):
        return [] 
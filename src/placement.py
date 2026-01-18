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
        placed = [c for c in self.circles if c.placed]
        open_points = []

        if len(placed) == 0:
            x = new_circle.radius
            y = new_circle.radius

            if self._is_valid(new_circle, x, y, placed):
                dist = np.sqrt(x*x + y*y)
                open_points.append((x,y,dist))

            return open_points
        
        return open_points 
    
    def _is_valid(self, circle, x, y, placed):

        if x - circle.radius < 0: return False
        if y - circle.radius < 0: return False
        if x + circle.radius > self.container.width: return False
        if y + circle.radius > self.container.height: return False

        for other in placed:
            dx = x - other.x
            dy = y - other.y
            d = np.sqrt(dx*dx + dy*dy)
            if d < (circle.radius + other.radius - 0.01):
                return False
            
        return True

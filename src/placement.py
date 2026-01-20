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
                cx = self.container.width / 2
                cy = self.container.height / 2
                best = min(open_points, key=lambda p: (p[0] - cx)**2 + (p[1] - cy)**2)
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
        
        if len(placed) == 1:
            c1 = placed[0]
            dist_centres = c1.radius + new_circle.radius

            for angle in np.linspace(0, 2*np.pi, 36, endpoint = False):
                x = c1.x + dist_centres * np.cos(angle)
                y = c1.y + dist_centres * np.sin(angle)

                if self._is_valid(new_circle, x, y, placed):
                    d0 = np.sqrt(x*x + y*y)
                    open_points.append((x, y, d0))

            return open_points 

        for i in range(len(placed)):
            for j in range(i + 1, len(placed)):
                c1 = placed[i]
                c2 = placed[j]

                positions = self.find_tangent_positions(c1, c2, new_circle)

                for (x,y) in positions:
                    if self._is_valid(new_circle, x, y, placed):
                        d0 = np.sqrt(x*x + y*y)
                        open_points.append((x,y,d0))
        
        if not open_points:
            for other in placed:
                dist_centres = other.radius + new_circle.radius 
                for angle in np.linspace(0, 2*np.pi, 36, endpoint = False):
                    x = other.x + dist_centres * np.cos(angle)
                    y = other.y + dist_centres * np.sin(angle)

                    if self._is_valid(new_circle, x, y, placed):
                        d0 = np.sqrt(x*x + y*y)
                        open_points.append((x, y, d0))
            
        
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
    
    def find_tangent_positions(self, c1, c2, new_circle):
        r1 = c1.radius + new_circle.radius
        r2 = c2.radius + new_circle.radius
        d = np.sqrt((c2.x - c1.x)**2 + (c2.y - c1.y)**2)
        
        if d == 0:
            return []
        if d > r1 + r2:
            return []
        if d < abs(r1 - r2):
            return []
        
        a = (r1**2 - r2**2 + d**2) / (2*d)
        h_sq = r1 ** 2 - a ** 2
        if h_sq < 0:
            h_sq = 0

        h = np.sqrt(h_sq) 

        px = c1.x + a * (c2.x - c1.x) / d
        py = c1.y + a * (c2.y - c1.y) / d

        positions = []

        if h > 1e-9:
            positions.append((
                px + h * (c2.y - c1.y) / d,
                py - h * (c2.x - c1.x) / d
            ))
            positions.append((
                px - h * (c2.y - c1.y) / d,
                py + h * (c2.x - c1.x) / d
            ))
        
        else:
            positions.append((px,py)) 
    
        return positions


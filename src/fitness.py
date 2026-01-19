import numpy as np

class FitnessEvaluator:
    def __init__(self, container):
        self.container = container

        self.com_min_x = 0.2 * container.width
        self.com_max_x = 0.8 * container.height
        self.com_min_y = 0.2 * container.height
        self.com_max_y = 0.8 * container.height

    def calculate_fitness(self, circles):

        placed  = [c for c in circles if c.placed]
        
        container_area = self.container.width * self.container.height
        circles_area = sum(np.pi * c.radius**2 for c in placed)
        wasted_space = container_area - circles_area

        penalty = 0

        overlap_count = 0
        for i in range(len(placed)):
            for j in range(i + 1, len(placed)):
                if placed[i].overlaps(placed[j]):
                    overlap_count += 1
        penalty += 1000 * overlap_count

        total_weight = sum(c.weight for c in placed)
        if total_weight > self.container.max_weight:
            penalty += 10000
        
        if total_weight > 0:
            com_x = sum(c.x * c.weight for c in placed) / total_weight
            com_y = sum(c.y * c.weight for c in placed) / total_weight

            if not (self.com_min_x <= com_x <= self.com_max_x and
                    self.com_min_y <= com_y <= self.com_max_y):
                penalty += 10000
        
        else:
            penalty += 10000
        
        return wasted_space + penalty
    
    # debug helper, exposes individual penalty components to identify which constraint causes large fitness values in testing
    def debug_fitness(self, circles):
        placed = [c for c in circles if c.placed]

        container_area = self.container.width * self.container.height
        circles_area = sum(np.pi * c.radius**2 for c in placed)
        wasted_space = container_area - circles_area

        overlap_count = 0
        for i in range(len(placed)):
            for j in range(i+1, len(placed)):
                if placed[i].overlaps(placed[j]):
                    overlap_count+=1

        boundary_violations = 0
        for c in placed:
            if (c.x - c.radius < 0 or c.y - c.radius < 0 or
                c.x + c.radius > self.container.width or
                c.y + c.radius > self.container.height):
                boundary_violations += 1
        
            total_weight = sum(c.weight for c in placed)
            weight_violation = int(total_weight > self.container.max_weight)

            com_violation = 1
            com_x = None
            com_y = None
            if total_weight > 0:
                com_x = sum(c.x * c.weight for c in placed) / total_weight
                com_y = sum(c.y * c.weight for c in placed) / total_weight
                com_violation = int(not (
                    self.com_min_x < com_x <= self.com_max_x and
                    self.com_min_y <= com_y <= self.com_max_y
                ))

            fitness = (wasted_space +
                1000 * overlap_count +
                1000 * boundary_violations +
                10000 * com_violation +
                10000 * weight_violation)

            return {
                "fitness" : fitness,
                "wasted_space" : wasted_space,
                "boundary_violations" : boundary_violations,
                "total_weight" : total_weight,
                "weight_violation" : weight_violation,
                "com_x" : com_x,
                "com_y" : com_y,
                "com_violation" : com_violation
            }

    
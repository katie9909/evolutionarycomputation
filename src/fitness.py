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
    
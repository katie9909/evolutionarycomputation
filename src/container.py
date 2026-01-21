class Container:
    def __init__(self, width, height, max_weight):
        self.width = float(width)
        self.height = float(height)
        self.max_weight = float(max_weight)

        self.com_min_x = 0.2 * self.width
        self.com_max_x = 0.8 * self.width
        self.com_min_y = 0.2 * self.height
        self.com_max_y = 0.8 * self.height

    def com_in_bounds(self,com_x,com_y):
        return (self.com_min_x <= com_x <= self.com_max_x and
                self.com_min_y <= com_y <= self.com_max_y)
    
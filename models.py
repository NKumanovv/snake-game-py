class Snake:
    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            head_y -= self.block_size
        elif self.direction == "DOWN":
            head_y += self.block_size
        elif self.direction == "LEFT":
            head_x -= self.block_size
        elif self.direction == "RIGHT":
            head_x += self.block_size

        self.body.insert(0, [head_x, head_y])

    def check_collision(self):
        head_x, head_y = self.body[0]
        
        if head_x < 0 or head_x >= self.bounds[0] or head_y < 0 or head_y >= self.bounds[1]:
            return True
            
        if self.body[0] in self.body[1:]:
            return True
            
        return False
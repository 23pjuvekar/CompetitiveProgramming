class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food[::-1]
        self.snake = deque()
        self.snake.append([0, 0])
        self.snake_size = 0
        self.directions = { "R" : [0, 1], "L" : [0, -1], "U" : [-1, 0], "D" : [1, 0] }

    def move(self, direction: str) -> int:
        head_row, head_col = self.snake[-1]
        new_row = head_row + self.directions[direction][0]
        new_col = head_col + self.directions[direction][1]
        if 0 > new_row or new_row == self.height or 0 > new_col or new_col == self.width:
            return -1
        if self.food and [new_row, new_col] == self.food[-1]: # Eating
            self.snake.append([new_row, new_col])
            self.food.pop()
            self.snake_size += 1
        else:
            self.snake.popleft()
            if [new_row, new_col] in self.snake:
                return -1
            self.snake.append([new_row, new_col])
        return self.snake_size



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

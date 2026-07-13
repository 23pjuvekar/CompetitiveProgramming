class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.q = deque()
        self.length = 0

    def next(self, val: int) -> float:
        if self.length == self.size:
            val_pop = self.q.popleft()
            self.sum -= val_pop
        else:
            self.length += 1

        self.sum += val
        self.q.append(val)

        return self.sum / self.length
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

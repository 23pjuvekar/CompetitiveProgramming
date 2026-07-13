class DetectSquares:

    def __init__(self):
        self.tracker = defaultdict(int)
        self.x_val = defaultdict(list)
        self.y_val = defaultdict(list)

    def add(self, point: List[int]) -> None:
        self.tracker[tuple(point)] += 1
        self.x_val[point[0]].append(point)
        self.y_val[point[1]].append(point)

    def count(self, point: List[int]) -> int:
        x_l = self.x_val[point[0]]
        y_l = self.y_val[point[1]]
        res = 0
        for x1, y1 in x_l:
            for x2, y2 in y_l:
                if abs(point[0] - x2) == abs(point[1] - y1) and abs(point[1] - y1) > 0:
                    res += self.tracker[(x2, y1)]   
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

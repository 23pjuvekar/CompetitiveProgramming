class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.table = defaultdict(list)
        self.n = len(grid)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                self.table[grid[r][c]].append(r)
                self.table[grid[r][c]].append(c)

    def adjacentSum(self, value: int) -> int:
        res = 0
        r, c = self.table[value]
        if r + 1 < self.n:
            res += self.grid[r+1][c]
        if c + 1 < self.n:
            res += self.grid[r][c+1]
        if 0 <= r - 1:
            res += self.grid[r-1][c]
        if 0 <= c - 1:
            res += self.grid[r][c-1]
        return res

    def diagonalSum(self, value: int) -> int:
        res = 0
        r, c = self.table[value]
        if r + 1 < self.n and c + 1 < self.n:
            res += self.grid[r+1][c + 1]
        if 0 <= r - 1 and 0 <= c - 1:
            res += self.grid[r-1][c-1]
        if r + 1 < self.n and 0 <= c - 1:
            res += self.grid[r+1][c-1]
        if 0 <= r - 1 and c + 1 < self.n:
            res += self.grid[r-1][c+1]
        return res
        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)

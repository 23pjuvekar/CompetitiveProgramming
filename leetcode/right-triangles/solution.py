class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:

        rows = defaultdict(int)
        cols = defaultdict(int)
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    res += (rows[r] - 1) * (cols[c] - 1)
        return res

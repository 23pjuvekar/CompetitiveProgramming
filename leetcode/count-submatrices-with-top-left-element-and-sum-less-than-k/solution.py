class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        res = 0
        for r in range(len(grid)):
            curr = 0
            for c in range(len(grid[0])):
                temp = grid[r][c]
                grid[r][c] = grid[r][c] + curr
                if r - 1 >= 0:
                    grid[r][c] += grid[r-1][c]
                if grid[r][c] <= k:
                    res += 1
                curr += temp
        return res

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        res = [[0] * (len(grid[0]) - 2) for _ in range(len(grid) - 2)]
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        res[i][j] = max(res[i][j], grid[r][c])
        return res

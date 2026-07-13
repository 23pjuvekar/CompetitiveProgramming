class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        res = []
        for c in range(len(grid[0])):
            good = True
            for r in range(len(grid)):
                if 0 > grid[r][c] + c or grid[r][c] + c >= len(grid[0]):
                    good = False
                    break
                elif grid[r][grid[r][c] + c] != grid[r][c]:
                    good = False
                    break
                else:
                    c = grid[r][c] + c
            if good:
                res.append(c)
            else:
                res.append(-1)
        return res

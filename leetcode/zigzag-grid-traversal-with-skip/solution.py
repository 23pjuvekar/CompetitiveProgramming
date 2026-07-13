class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:

        read = True
        reverse = False
        ROWS = len(grid)
        COLS = len(grid[0])
        res = []

        for r in range(ROWS):
            if reverse:
                for c in range(COLS - 1, -1, -1):
                    if read:
                        res.append(grid[r][c])
                        read = False
                    else:
                        read = True
                reverse = False
            else:
                for c in range(COLS):
                    if read:
                        res.append(grid[r][c])
                        read = False
                    else:
                        read = True
                reverse = True
        
        return res

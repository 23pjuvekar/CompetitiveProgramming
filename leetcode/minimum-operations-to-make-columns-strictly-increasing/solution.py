class Solution(object):
    def minimumOperations(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        for c in range(COLS):
            min_val = grid[0][c]
            for r in range(1, ROWS):
                if grid[r][c] <= min_val:
                    res += (min_val + 1) - grid[r][c]
                    min_val += 1
                else:
                    min_val = grid[r][c]

        return res

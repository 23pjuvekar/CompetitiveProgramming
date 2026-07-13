class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:

        f_r = float("inf")
        l_r = float("-inf")
        f_c = float("inf")
        l_c = float("-inf")


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    f_r = min(f_r, r)
                    f_c = min(f_c, c)
                    l_r = max(l_r, r)
                    l_c = max(l_c, c)
        return (l_r - f_r + 1) * (l_c - f_c + 1)

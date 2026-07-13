class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        r_dp = [0] * R
        c_dp = [0] * C
        res = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    r_dp[r] += 1
                    c_dp[c] += 1
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and max(r_dp[r], c_dp[c]) > 1:
                    res += 1
        
        return res

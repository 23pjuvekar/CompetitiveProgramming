class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        MOD = 10**9 + 7
        dp = {}

        def dfs(r, c, current_sum_mod_k):
            if r >= n or c >= m:
                return 0
            current_sum_mod_k = (current_sum_mod_k + grid[r][c]) % k
            if r == n - 1 and c == m - 1:
                return 1 if current_sum_mod_k == 0 else 0
            if (r, c, current_sum_mod_k) in dp:
                return dp[(r, c, current_sum_mod_k)]
            paths = (dfs(r + 1, c, current_sum_mod_k) +
                     dfs(r, c + 1, current_sum_mod_k)) % MOD

            dp[(r, c, current_sum_mod_k)] = paths
            return paths

        return dfs(0, 0, 0)

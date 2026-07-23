class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                entry = (i + 1) * (j + 1)
                best = float('inf')

                if i > 0:
                    cost = dp[i - 1][j]
                    if not (i - 1 == 0 and j == 0):
                        cost += waitCost[i - 1][j]
                    best = min(best, cost)

                if j > 0:
                    cost = dp[i][j - 1]
                    if not (i == 0 and j - 1 == 0):
                        cost += waitCost[i][j - 1]
                    best = min(best, cost)

                dp[i][j] = entry + best

        return dp[m - 1][n - 1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                else:
                    if 0 <= r - 1 < m:
                        dp[r][c] += dp[r - 1][c]
                    if 0 <= c - 1 < n:
                        dp[r][c] += dp[r][c - 1]
        return dp[-1][-1]

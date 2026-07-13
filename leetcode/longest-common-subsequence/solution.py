class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        ROWS = len(text1) + 1
        COLS = len(text2) + 1

        dp = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS - 2, -1, -1):
            for c in range(COLS - 2, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r][c + 1], dp[r + 1][c])


        return dp[0][0]

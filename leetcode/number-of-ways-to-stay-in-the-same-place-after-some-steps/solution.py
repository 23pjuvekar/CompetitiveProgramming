class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_pos = min(steps + 1, arrLen)
        dp = [0] * max_pos
        dp[0] = 1
        MOD = 10**9 + 7
        while steps > 0:
            dp_new = [0] * max_pos
            for i in range(max_pos):
                if 0 <= i - 1 < max_pos:
                    dp_new[i] += (dp[i-1] % MOD)
                if 0 <= i + 1 < max_pos:
                    dp_new[i] += (dp[i+1] % MOD)
                dp_new[i] += (dp[i] % MOD)
            dp = dp_new
            steps -= 1
        return dp[0] % MOD

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        n = len(s)
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            for j in range(i, n):
                num = int(s[i:j+1])
                if num > k:
                    break
                dp[i] = (dp[i] + dp[j + 1]) % MOD
        return dp[0] % MOD

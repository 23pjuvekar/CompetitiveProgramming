class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        dp = defaultdict(int)
        for t in time:
            dp[t % 60] += 1
        res = 0
        res += (dp[0] * (dp[0] - 1)) // 2
        res += (dp[30] * (dp[30] - 1)) // 2
        for i in range(1, 30):
            res += dp[60 - i] * dp[i]
        return res

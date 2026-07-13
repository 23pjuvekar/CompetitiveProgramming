class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:

        dp = defaultdict(int)
        for h in hours:
            dp[h % 24] += 1
        print(dp)
        res = 0
        res += (dp[0] * (dp[0] - 1)) // 2
        res += (dp[12] * (dp[12] - 1)) // 2
        for i in range(1, 12):
            res += dp[24 - i] * dp[i]
        return res

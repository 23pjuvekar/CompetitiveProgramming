class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        coins = [0, 0] + list(sorted(count.keys()))
        dp = [0] * len(coins)
        for i in range(2, len(coins)):
            if coins[i] - coins[i - 1] > 1:
                dp[i] = dp[i-1] + (coins[i] * count[coins[i]])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + (coins[i] * count[coins[i]]))
        return dp[-1]
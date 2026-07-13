class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        dp = [1] + [0] * (n-1)
        mod = 10 ** 9 + 7
        share = 0

        for i in range(1, n):
            new_sharers = dp[i - delay]
            forgetters = dp[i - forget]
            share = share + new_sharers - forgetters
            dp[i] = share
        
        return sum(dp[-forget:]) % mod

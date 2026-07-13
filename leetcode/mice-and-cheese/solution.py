class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:

        res = sum(reward2)
        dp = []
        for r1, r2 in zip(reward1, reward2):
            dp.append(r1 - r2)
        dp.sort(reverse=True)
        for i in range(k):
            res += dp[i]
        return res

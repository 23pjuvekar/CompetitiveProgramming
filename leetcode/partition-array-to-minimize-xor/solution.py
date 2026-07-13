class Solution:
    def minXor(self, nums: List[int], k: int) -> int:

        n = len(nums)
        px = [0] * (n + 1)
        for i in range(1, n + 1):
            px[i] = px[i - 1] ^ nums[i - 1]
    
        INF = 10**18
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
    
        for i in range(1, n + 1):
            for p in range(1, min(i, k) + 1):
                best = INF
                for j in range(p - 1, i):
                    seg_xor = px[i] ^ px[j]
                    cost = max(dp[j][p - 1], seg_xor)
                    if cost < best:
                        best = cost
                dp[i][p] = best
    
        return dp[n][k]

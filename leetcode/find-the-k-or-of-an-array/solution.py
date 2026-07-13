class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        dp = [0]*31
        for num in nums:
            i = 0    
            while num > 0:
                dp[i] += (num % 2)
                i += 1
                num = num // 2
        res = 0
        for c in reversed(dp):
            res = res * 2
            if c >= k:
                res += 1
        return res

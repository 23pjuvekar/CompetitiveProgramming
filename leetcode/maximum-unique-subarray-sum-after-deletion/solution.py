class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = 0
        for c in set(nums):
            if c > 0:
                res += c
        if res == 0:
            return max(nums)
        return res

class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:

        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        while l < r:
            res += nums[r - 1]
            r -= 2
            l += 1
        return res

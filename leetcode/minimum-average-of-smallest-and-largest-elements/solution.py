class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        nums.sort()
        res = float("inf")
        l = 0
        r = len(nums) - 1

        while l < r:
            res = min(res, (nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return res

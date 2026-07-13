class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        res = abs(nums[0] - nums[-1])

        for i in range(len(nums) - 1):
            res = max(abs(nums[i] - nums[i+1]), res)

        return res

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:

        nums.sort()
        res = float("inf")
        for i in range(len(nums) - 1):
            res = min(res, nums[i + 1] - nums[i])
        return res

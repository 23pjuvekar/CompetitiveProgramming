class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        res = nums[0]
        curr = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 0:
                curr += nums[i + 1]
                res = max(res, curr)
            else:
                curr = nums[i + 1]
                res = max(res, curr)

        return res

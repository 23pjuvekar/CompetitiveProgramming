class Solution:
    def maxScore(self, nums: List[int]) -> int:

        total = sum(nums)
        res = float("inf")
        if len(nums) % 2 == 1:
            for num in nums:
                res = min(num, res)
        else:
            for i in range(len(nums) - 1):
                res = min(res, nums[i] + nums[i + 1])
        return total - res

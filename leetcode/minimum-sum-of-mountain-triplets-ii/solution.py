class Solution:
    def minimumSum(self, nums: List[int]) -> int:

        min_before = [float("inf")] * len(nums)
        min_after = [float("inf")] * len(nums)
        for i in range(1, len(nums)):
            min_before[i] = min(min_before[i - 1], nums[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            min_after[i] = min(min_after[i + 1], nums[i + 1])
        print(min_before, min_after)
        res = float("inf")
        for i in range(1, len(nums) - 1):
            if min_before[i] < nums[i] and nums[i] > min_after[i]:
                res = min(res, nums[i] + min_before[i] + min_after[i])
        if res == float("inf"):
            return -1
        return res

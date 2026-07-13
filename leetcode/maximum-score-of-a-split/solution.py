class Solution:
    def maximumScore(self, nums: List[int]) -> int:

        prefix = nums.copy()
        for i in range(1, len(nums)):
            prefix[i] += prefix[i - 1]
        min_val = nums.copy()
        for i in range(len(nums) - 2, -1, -1):
            min_val[i] = min(min_val[i + 1], min_val[i])
        print(min_val)
        res = float("-inf")
        for i in range(len(nums) - 1):
            res = max(res, prefix[i] - min_val[i+1])
        return res

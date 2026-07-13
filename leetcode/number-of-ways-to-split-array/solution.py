class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        total = sum(nums)
        res = 0
        prev_sum = 0

        for i in range(len(nums) - 1):
            prev_sum += nums[i]
            total -= nums[i]
            if prev_sum >= total:
                res += 1
        
        return res

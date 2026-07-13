class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        total = sum(nums)
        prev_total = 0
        for i in range(len(nums)):
            res[i] = (total - (len(nums) - i) * nums[i]) + (nums[i] * i - prev_total)
            total -= nums[i]
            prev_total += nums[i]
        return res

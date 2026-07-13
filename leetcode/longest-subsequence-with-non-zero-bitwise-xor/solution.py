class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        
        if max(nums) == 0:
            return 0
        total = nums[0]
        for i in range(1, len(nums)):
            total = total ^ nums[i]
        if total == 0:
            return len(nums) - 1
        else:
            return len(nums)

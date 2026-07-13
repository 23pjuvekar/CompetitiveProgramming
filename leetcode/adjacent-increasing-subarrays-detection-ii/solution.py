class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        prev = 0
        curr = 1
        res = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            res = max(res, curr // 2, min(prev, curr))
        
        return res

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        k = max(nums)
        res = 0
        l = 0
        curr = nums[0]
        for r in range(len(nums)):
            curr = curr & nums[r]
            if curr != k:
                curr = nums[r]
                l = r
            res = max(res, r - l + 1)
        return res

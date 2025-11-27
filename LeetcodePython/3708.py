class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        res = 2
        curr_length = 2

        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                curr_length += 1
                res = max(res, curr_length)
            else:
                curr_length = 2
        return res

        
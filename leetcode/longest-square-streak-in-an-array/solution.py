class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        nums_value = set(nums)
        res = 1
        curr_res = 1
        for num in nums:
            curr_res = 1
            while num ** 2 in nums_value:
                num = num ** 2
                curr_res += 1
            res = max(res, curr_res)
        if res == 1:
            return -1
        return res

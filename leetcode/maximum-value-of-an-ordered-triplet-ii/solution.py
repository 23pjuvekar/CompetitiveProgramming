class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        max_diff = 0
        max_i = 0
        for num in nums:
            res = max(res, max_diff * num)        
            max_diff = max(max_diff, max_i - num) 
            max_i = max(max_i, num)               

        return res

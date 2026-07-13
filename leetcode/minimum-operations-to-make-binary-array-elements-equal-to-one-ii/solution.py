class Solution:
    def minOperations(self, nums: List[int]) -> int:

        res = 0
        if nums[0] == 0:
            res += 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                res += 1
        return res

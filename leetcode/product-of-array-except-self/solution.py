{1, 2, 3, 4}
{1, 1, 2, 6}
{24, 12, 4, 1}

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        prefix = 1
        for i in range(len(nums) - 2, -1, -1):
            prefix *= nums[i+1]
            res[i] *= prefix
            
        
        return res

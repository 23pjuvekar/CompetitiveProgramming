class Solution:
    def missingInteger(self, nums: list[int]) -> int: 

        initial_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                initial_sum += nums[i]
            else:
                break
        
        nums_set = set(nums)
        ans = initial_sum
        while ans in nums_set:
            ans += 1
            
        return ans

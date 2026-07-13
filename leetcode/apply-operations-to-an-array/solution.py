class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            
        zero_c = 0
        for n in nums:
            if n == 0:
                zero_c += 1
        
        for i in range(zero_c):
            nums.remove(0)
        
        for i in range(zero_c):
            nums.append(0)
        
        return nums

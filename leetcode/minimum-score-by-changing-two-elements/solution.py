class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()

        change_two_largest  = nums[-3] - nums[0]
        change_two_smallest = nums[-1] - nums[2]    
        change_both_ends    = nums[-2] - nums[1]  

        return min(change_two_largest, change_two_smallest, change_both_ends)

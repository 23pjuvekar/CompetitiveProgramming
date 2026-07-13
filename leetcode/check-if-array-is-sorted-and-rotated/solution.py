class Solution:
    def check(self, nums: List[int]) -> bool:

        decrease_count = 0

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                decrease_count += 1
                if decrease_count == 2:
                    return False
            
        if nums[-1] > nums[0]:
                decrease_count += 1
                if decrease_count == 2:
                    return False
                    
        return True

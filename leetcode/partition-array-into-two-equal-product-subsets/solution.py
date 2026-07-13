class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:


        def backtrack(values_1, values_2, i):
            if values_1 == target and values_2 == target and i == len(nums):
                return True
            if values_1 > target or values_2 > target or i == len(nums):
                return False
            return backtrack(values_1 * nums[i], values_2, i + 1) or \
                backtrack(values_1, values_2 * nums[i], i + 1)
        
        return backtrack(1, 1, 0)

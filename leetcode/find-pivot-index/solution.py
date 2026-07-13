class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left = 0
        for index, value in enumerate(nums):
            if total_sum - value == left:
                return index
            total_sum -= value
            left += value
        
        return -1

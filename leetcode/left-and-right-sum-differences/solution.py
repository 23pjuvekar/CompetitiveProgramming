class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        right = sum(nums)
        left = 0
        res = []
        for i in range(len(nums)):
            right -= nums[i]
            res.append(abs(right - left))
            left += nums[i]
        return res

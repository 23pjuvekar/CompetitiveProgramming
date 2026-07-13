class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        max_length = -1
        left = 0
        while left + 1 < len(nums):
            if nums[left] + 1 == nums[left + 1]:
                right = left + 1
                diff = 1
                while right < len(nums) and nums[right] - nums[right - 1] == diff:
                    right += 1
                    diff *= -1
                max_length = max(max_length, right - left)
                left = right - 1
            else:
                left += 1
        return max_length

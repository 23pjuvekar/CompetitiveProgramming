class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        i = len(nums) - 2
        while i >= 0:
            if nums[i + 1] > nums[i]:
                i -= 1
            else:
                break
        return i + 1

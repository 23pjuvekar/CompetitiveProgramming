class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:

        start = max(nums[:len(nums) - k + 1])
        return nums[nums.index(start):nums.index(start)+k]

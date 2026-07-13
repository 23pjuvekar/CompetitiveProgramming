class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        return abs(sum(nums[:k]) - sum(nums[-k:]))

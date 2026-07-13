class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        if min(nums) == k:
            return len(set(nums)) - 1
        elif min(nums) > k:
            return len(set(nums))
        return -1

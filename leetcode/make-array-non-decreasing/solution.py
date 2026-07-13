class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:

        max_last = float("-inf")
        res = len(nums)
        for num in nums:
            if num < max_last:
                res -= 1
            max_last = max(max_last, num)
        return res

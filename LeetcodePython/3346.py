from bisect import bisect_left, bisect_right
from collections import Counter


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        res = 0
        counter = Counter(nums)
        for i in range(nums[0], nums[-1] + 1):
            left = bisect_left(nums, i - k)
            right = bisect_right(nums, i + k)
            res = max(res, min(right - left, counter[i] + numOperations))
        return res
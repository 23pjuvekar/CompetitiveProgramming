class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        res = float("inf")
        total = 0
        for num in nums:
            total += num
            res = min(res, total)
        if res > 0:
            return 1
        return -(res) + 1

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)
        for i in range(len(nums)):
            if n % (i + 1) == 0:
                res += (nums[i] ** 2)
        return res

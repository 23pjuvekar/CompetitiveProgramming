class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:

        nums.sort(reverse=True)
        res = 0
        for num in nums[:k]:
            res += num * max(mul, 1)
            mul -= 1
        return res

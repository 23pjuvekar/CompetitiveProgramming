class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        res = 0
        for num in nums:
            if num % 2 != 1:
                res += 1
        return res > 1

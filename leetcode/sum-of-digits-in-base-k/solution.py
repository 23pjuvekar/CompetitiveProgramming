class Solution:
    def sumBase(self, n: int, k: int) -> int:

        res = 0

        while n != 0:
            quot = n // k
            remainder = n % k
            res += remainder
            n = quot

        return res

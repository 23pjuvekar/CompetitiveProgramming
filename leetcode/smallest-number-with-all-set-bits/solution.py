class Solution:
    def smallestNumber(self, n: int) -> int:
        b = 0
        while n:
            b += 1
            n = n // 2
        return (1 << b) - 1

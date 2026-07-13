class Solution:
    def minOperations(self, n: int) -> int:

        if n % 2 == 1:
            n = n // 2
            return (n) * (n + 1)
        else:
            n = n // 2
            return (n) * (n + 1) - n

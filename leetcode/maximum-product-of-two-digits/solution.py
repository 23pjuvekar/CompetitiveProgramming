class Solution:
    def maxProduct(self, n: int) -> int:

        values = []
        while n:
            values.append(n % 10)
            n = n // 10
        values.sort(reverse=True)
        return values[0] * values[1]

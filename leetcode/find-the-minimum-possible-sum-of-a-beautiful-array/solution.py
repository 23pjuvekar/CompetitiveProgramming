class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        k = target // 2
        if n <= k:
            return (n * (n + 1) // 2) % (10 ** 9 + 7)
        return ((k * (k + 1) // 2 + (target + target + n - k - 1) * (n - k) // 2)) % (10 ** 9 + 7)

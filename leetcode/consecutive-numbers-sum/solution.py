class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:

        # n = x * k + (k) * (k + 1) / 2
        # x = n/k - (k+1)/2
        # Need to be int as well so just count.
        # x > 0
        # n/k - (k+1)/2 > 0
        # 2*n > k**2 + k
        # 2*n + 1/4 > (k + 1/2) ** 2
        # sqrt(2*n + 1/4) > (k + 1/2)
        # sqrt(2*n + 1/4) - 1/2 > k
        # Limit

        res = 0
        limit = ceil((2 * n + 0.25)**0.5 - 0.5)
        for k in range(1, limit + 1):
            if (n / k - (k + 1) / 2) % 1 == 0:
                res += 1
        return res

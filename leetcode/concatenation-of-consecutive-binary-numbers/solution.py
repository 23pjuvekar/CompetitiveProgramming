class Solution:
    def concatenatedBinary(self, n: int) -> int:

        def lengthBinary(n):
            res = 0
            while n > 0:
                n = n // 2
                res += 1
            return res

        mod = (10 ** 9 ) + 7
        curr = 1
        res = 0
        while curr <= n:
            res = (res * (2 ** lengthBinary(curr)) + curr) % mod
            curr += 1

        return res % mod

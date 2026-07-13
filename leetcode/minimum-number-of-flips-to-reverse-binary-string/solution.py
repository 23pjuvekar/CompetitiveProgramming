class Solution:
    def minimumFlips(self, n: int) -> int:

        res = 0
        for x, c in zip(bin(n)[2:], bin(n)[2:][::-1]):
            if x != c:
                res += 1
        return res

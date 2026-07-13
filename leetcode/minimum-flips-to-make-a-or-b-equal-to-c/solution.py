class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            if c % 2 == 0:
                if a % 2 == 1:
                    res += 1
                if b % 2 == 1:
                    res += 1
            else:
                if a % 2 == 0 and b % 2 == 0:
                    res += 1
            a = a // 2
            b = b // 2
            c = c // 2
        return res

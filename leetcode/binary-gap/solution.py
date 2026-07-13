class Solution:
    def binaryGap(self, n: int) -> int:

        last = -1
        res = 0
        i = 0
        while n:
            if n % 2 == 1:
                if last == -1:
                    last = i
                else:
                    res = max(res, i - last)
                    last = i
            n = n // 2
            i += 1
        return res

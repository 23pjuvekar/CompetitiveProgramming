class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def getPower(n):
            step = 0
            while n != 1:
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = n * 3 + 1
                step += 1
            return step

        res = []
        for i in range(lo, hi + 1):
            res.append((getPower(i), i))
        res.sort()
        print(res)
        return res[k-1][1]

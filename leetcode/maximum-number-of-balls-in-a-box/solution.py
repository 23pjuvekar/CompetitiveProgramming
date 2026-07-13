class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        c1 = defaultdict(int)
        res = 0
        for i in range(lowLimit, highLimit + 1):
            total = 0
            for c in str(i):
                total += int(c)
            c1[total] += 1
            res = max(res, c1[total])
        return res

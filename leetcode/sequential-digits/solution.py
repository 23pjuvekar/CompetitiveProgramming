class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        s = len(str(low))
        e = len(str(high)) + 1
        res = []

        for i in range(s, e):
            for x in range(1, 10):
                if x + i <= 10:
                    curr = 0
                    for d in range(x, x + i):
                        curr *= 10
                        curr += d
                    if low <= curr <= high:
                        res.append(curr)
        return res

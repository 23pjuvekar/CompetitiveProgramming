class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for b in range(2, n + 1):
            for u in range(1, b):
                good = True
                for i in range(2, u + 1):
                    if b % i == 0 and u % i == 0:
                        good = False
                if good:
                    res.append(str(u) + "/" + str(b))
        res.sort()
        return res

class Solution:
    def checkGoodInteger(self, n: int) -> bool:

        d = 0
        s = 0
        for c in str(n):
            d += int(c)
            s += int(c) * int(c)
        
        return s - d >= 50

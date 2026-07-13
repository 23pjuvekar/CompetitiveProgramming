class Solution:
    def alternateDigitSum(self, n: int) -> int:
        positive = True
        res = 0
        for c in str(n):
            if positive:
                res += int(c)
                positive = False
            else:
                res -= int(c)
                positive = True 
        return res

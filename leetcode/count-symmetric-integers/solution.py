class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        res = 0
        for i in range(low, high + 1):
            num = str(i)
            n = len(num)
            summ = 0
            for c in num[:n//2]:
                summ += int(c)
            for c in num[n//2:]:
                summ -= int(c)
            if n % 2 == 0 and summ == 0:
                res += 1
        return res

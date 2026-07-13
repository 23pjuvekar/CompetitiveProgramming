class Solution:
    def bitwiseComplement(self, n: int) -> int:

        res = ""
        if n == 0:
            res = "1"
        while n:
            if n % 2 == 0:
                res += "1"
            else:
                res += "0"
            n = n // 2
        
        final = 0
        for c in res[::-1]:
            final = final * 2 + int(c)
        return final

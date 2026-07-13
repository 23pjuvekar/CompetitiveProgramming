class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        nines, rem = divmod(sum, 9)
        print(nines, rem)

        if nines > num or (nines == num and rem != 0):
            return ""
        
        if nines == num and rem == 0:
            return "9" * nines

        res = ""
        i = 0

        while i < num:
            if nines > 0:
                res += "9"
                nines -= 1
            else:
                res += str(rem)
                rem = "0"
            i += 1
        return res

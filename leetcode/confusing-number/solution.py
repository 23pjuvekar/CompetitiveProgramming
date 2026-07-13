class Solution:
    def confusingNumber(self, n: int) -> bool:

        res = ""
        n = str(n)
        for c in n:
            if c in "23457":
                return False
            elif c == "6":
                res += "9"
            elif c == "9":
                res += "6"
            else:
                res += c
        return res != n[::-1]

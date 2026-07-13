class Solution:
    def generateTheString(self, n: int) -> str:

        res = ""
        if n % 2 == 1:
            for _ in range(n):
                res += "a"
        else:
            for _ in range(n - 1):
                res += "a"
            res += "b"
        return res

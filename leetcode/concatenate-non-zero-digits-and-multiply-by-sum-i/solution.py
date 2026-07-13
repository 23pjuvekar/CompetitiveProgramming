class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res = ""
        multiple = 0
        for c in str(n):
            if c != "0":
                res += c
                multiple += int(c)
        if res == "":
            return 0
        return int(res) * multiple

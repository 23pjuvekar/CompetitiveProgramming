class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        res = 0

        for c in columnTitle:
            res *= 26
            res += int(ord(c) - 64)
        
        return res

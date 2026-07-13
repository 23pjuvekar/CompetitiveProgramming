class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i + 1] in "1234567890":
                res += s[i]
                res += chr(ord(s[i]) + int(s[i+1]))
                i += 2
            else:
                res += s[i]
                i += 1
        return res

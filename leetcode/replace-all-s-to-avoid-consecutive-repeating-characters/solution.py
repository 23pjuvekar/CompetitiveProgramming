class Solution:
    def modifyString(self, s: str) -> str:

        res = ""

        for i in range(len(s)):
            if s[i] == "?":
                for c in "qwertyuioplkjhgfdsazxcvbnm":
                    good = True
                    if i > 0 and res[i - 1] == c:
                        good = False
                    if i < len(s) - 1 and s[i + 1] == c:
                        good = False
                    if good:
                        res += c
                        break
            else:
                res += s[i]
        return res

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        parts = [""]
        d = 0
        p = 0
        for c in s:
            parts[-1] += c
            if c == "(":
                p += 1
            else:
                d += 1
            if d == p:
                parts.append("")
                d = 0
                p = 0
        res = ""
        for part in parts:
            if len(part) != 0:
                res += part[1:len(part) - 1]
        return res

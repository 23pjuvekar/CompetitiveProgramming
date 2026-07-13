class Solution:
    def toLowerCase(self, s: str) -> str:

        res = ""
        for c in s:
            res += c.lower()
        return res

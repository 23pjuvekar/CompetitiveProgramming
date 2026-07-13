class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        res = ""
        for c in s:
            res += c
            if res[-len(part):] == part:
                res = res[:len(res)-len(part)]
        return res

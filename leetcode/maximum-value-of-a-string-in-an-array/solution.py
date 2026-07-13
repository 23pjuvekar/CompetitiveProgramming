class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        res = 0
        for s in strs:
            digit = True
            for c in s:
                if c not in "0123456789":
                    digit = False
                    break
            if digit:
                res = max(res, int(s))
            else:
                res = max(res, len(s))
        return res

class Solution:
    def partitionString(self, s: str) -> int:

        seen = set()
        res = 1
        for c in s:
            if c not in seen:
                seen.add(c)
            else:
                res += 1
                seen.clear()
                seen.add(c)
        return res

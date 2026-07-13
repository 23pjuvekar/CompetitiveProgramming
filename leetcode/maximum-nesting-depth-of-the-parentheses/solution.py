class Solution:
    def maxDepth(self, s: str) -> int:

        cnt = 0
        res = 0
        for c in s:
            if c == "(":
                cnt += 1
                res = max(res, cnt)
            elif c == ")":
                cnt -= 1
        return res

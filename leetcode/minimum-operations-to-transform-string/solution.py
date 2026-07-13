class Solution:
    def minOperations(self, s: str) -> int:

        res = 0
        for c in set(s):
            if c != "a":
                res = max(res, ord("z") - ord(c) + 1)
        return res

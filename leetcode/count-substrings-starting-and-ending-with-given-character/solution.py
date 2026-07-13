class Solution:
    def countSubstrings(self, s: str, c: str) -> int:

        amt = s.count(c)
        if amt == 1:
            return 1
        return ((amt) * (amt + 1)) // 2

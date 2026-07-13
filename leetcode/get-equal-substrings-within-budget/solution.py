class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        res = 0
        l = 0
        curr_total = 0
        for r in range(len(s)):
            curr_total += abs(ord(s[r]) - ord(t[r]))
            while curr_total > maxCost:
                curr_total -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, r - l + 1)
        return res

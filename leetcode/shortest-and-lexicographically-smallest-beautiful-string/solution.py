class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        l = 0
        curr_total = 0
        res = ""
        length = float("inf")
        for r in range(len(s)):
            if s[r] == "1":
                curr_total += 1
            while curr_total > k:
                if s[l] == "1":
                    curr_total -= 1
                l += 1
            while l <= r and s[l] != "1":
                l += 1
            if curr_total == k and r - l + 1 < length:
                res = s[l:r+1]
                length = r - l + 1
            if curr_total == k and r - l + 1 == length:
                res = min(res, s[l:r+1])
        return res

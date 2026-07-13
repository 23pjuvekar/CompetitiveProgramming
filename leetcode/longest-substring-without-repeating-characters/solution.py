# Sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        tracker = set()

        for r in range(len(s)):
            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1
            tracker.add(s[r])
            res = max(res, r - l + 1)

        
        return res

class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        l = 0
        window = set()
        res = 0
        for r in range(len(s)):
            if r - l + 1 == 4:
                window.remove(s[l])
                l += 1
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            if r - l + 1 == 3:
                print(s[l:r+1])
                res += 1
        return res

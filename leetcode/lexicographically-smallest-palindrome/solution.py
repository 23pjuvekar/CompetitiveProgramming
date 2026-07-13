class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        res = [0] * len(s)
        while l <= r:
            if s[l] > s[r]:
                res[l] = s[r]
                res[r] = s[r]
            else:
                res[l] = s[l]
                res[r] = s[l]
            l += 1
            r -= 1
        return "".join(res)

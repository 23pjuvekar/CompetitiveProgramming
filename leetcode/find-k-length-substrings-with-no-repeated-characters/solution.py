class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        window = set()
        l = 0
        res = 0
        for r in range(len(s)):
            print(r)
            if r - l + 1 > k:
                window.remove(s[l])
                l += 1
            if s[r] in window:
                while s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                window.remove(s[l])
                l += 1
            window.add(s[r])
            if r - l + 1 == k:
                res += 1
        return res

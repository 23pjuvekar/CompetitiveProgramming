class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        l = 0
        len_1 = 0
        len_0 = 0
        for r in range(len(s)):
            if s[l] != s[r]:
                l = r
            if s[r] == "1":
                len_1 = max(len_1, r - l + 1)
            if s[r] == "0":
                len_0 = max(len_0, r - l + 1)
        return len_1 > len_0

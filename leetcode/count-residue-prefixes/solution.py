class Solution:
    def residuePrefixes(self, s: str) -> int:

        letters = set()
        res = 0
        for i in range(len(s)):
            letters.add(s[i])
            if (i + 1) % 3 == len(letters):
                res += 1
        return res

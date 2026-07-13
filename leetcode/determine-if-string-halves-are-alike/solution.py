class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        s = s.lower()
        n = len(s)
        n = n // 2
        res = 0
        vowels = set("aeiou")
        for i, c in enumerate(s):
            if i < n and c in vowels:
                res += 1
            elif i >= n and c in vowels:
                res -= 1
        return res == 0

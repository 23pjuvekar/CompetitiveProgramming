class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        s = defaultdict(int)
        for c in word:
            if c.islower() and s[c.lower()] == 0:
                s[c.lower()] = 1
            elif c.isupper() and s[c.lower()] == 1:
                s[c.lower()] = 2
            elif c.islower() and s[c.lower()] == 2 or c.isupper() and s[c.lower()] == 0:
                s[c.lower()] = -1
        res = 0
        for k, v in s.items():
            if v == 2:
                print(k)
                res += 1
        return res

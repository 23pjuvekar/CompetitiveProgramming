class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s_c = Counter(s)

        for char, value in Counter(t).items():
            if value != s_c[char]:
                return char

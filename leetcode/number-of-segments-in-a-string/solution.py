class Solution:
    def countSegments(self, s: str) -> int:

        res = 0
        word = 0

        for c in s:
            if c == " ":
                res += word
                word = 0
            else:
                word = 1
        return res + word

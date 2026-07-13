class Solution:
    def stringHash(self, s: str, k: int) -> str:

        res = ""
        n = len(s)
        for i in range(0, n, k):
            total = 0
            for c in s[i:i+k]:
                total += ord(c) - ord("a")
            total = total % 26
            res += chr(ord("a") + total)
        return res

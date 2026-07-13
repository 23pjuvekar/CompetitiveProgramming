class Solution:
    def minSteps(self, s: str, t: str) -> int:

        c1 = Counter(s)
        c2 = Counter(t)
        res = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            res += abs(c1[c] - c2[c])
        return res

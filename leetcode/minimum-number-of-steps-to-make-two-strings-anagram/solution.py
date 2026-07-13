class Solution:
    def minSteps(self, s: str, t: str) -> int:

        s1 = Counter(s)
        t2 = Counter(t)
        v = set(t)
        res = len(s)
        for c in v:
            res -= min(s1[c], t2[c])
        return res

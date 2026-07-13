class Solution:
    def maxFreqSum(self, s: str) -> int:

        count = Counter(s)
        m = 0
        n = 0
        for x in "aeiou":
            m = max(m, count[x])
        for x in "qwrtypsdfghjklzxcvbnm":
            n = max(n, count[x])
        return n + m

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        res = 0
        for d, f in Counter(str(n)).items():
            res += int(d) * f
        return res

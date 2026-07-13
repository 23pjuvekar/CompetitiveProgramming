class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:

        weight.sort()

        total = 0
        res = 0
        for w in weight:
            total += w
            if total <= 5000:
                res += 1
        return res

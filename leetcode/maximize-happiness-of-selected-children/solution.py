class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        happiness.sort(reverse=True)
        res = 0
        i = 0
        for c in range(k):
            h = happiness[c]
            res += max(h - i, 0)
            i += 1
        return res

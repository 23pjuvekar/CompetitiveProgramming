class Solution:
    def getLargestOutlier(self, A: List[int]) -> int:
        total = sum(A)
        count = Counter(A)
        res = -inf
        for a in A:
            outlier = total - (2 * a)
            if count[outlier] > (outlier == a):
                res = max(res, outlier)
        return res

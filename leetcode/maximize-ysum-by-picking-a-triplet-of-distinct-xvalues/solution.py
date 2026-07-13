class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:

        a = [[yi, xi] for xi, yi in zip(x, y)]
        a.sort(reverse=True)
        res = 0
        used = set()
        for yi, xi in a:
            if xi in used:
                continue
            res += yi
            used.add(xi)
            if len(used) == 3:
                break
        if len(used) != 3:
            return -1
        return res

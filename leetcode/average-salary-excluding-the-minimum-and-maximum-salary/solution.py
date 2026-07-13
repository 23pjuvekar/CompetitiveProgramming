class Solution:
    def average(self, salary: List[int]) -> float:

        total = 0
        mi = float("inf")
        ma = float("-inf")
        for s in salary:
            total += s
            mi = min(mi, s)
            ma = max(ma, s)

        return (total - mi - ma) / (len(salary) - 2)

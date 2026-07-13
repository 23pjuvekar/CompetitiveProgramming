class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:

        res = 0
        for i in range(0, (total // cost1) + 1):
            res += ((total - (cost1 * i)) // cost2) + 1
        return res

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:

        l = 0
        r = budget + max(stock)
        res = 0

        while l <= r:
            m = (r + l) // 2
            good = False
            for i in range(len(composition)):
                total_cost = 0
                for j in range(len(composition[i])):
                    total_cost += max(0, (m * composition[i][j] - stock[j]) * cost[j])
                if total_cost <= budget:
                    good = True
                    break
            if good:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res

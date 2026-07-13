class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        n_min = min(need1, need2)
        n_max = max(need1, need2)
        
        ans = (need1 * cost1) + (need2 * cost2)
        ans = min(ans, (n_min * costBoth) + ((need1 - n_min) * cost1) + ((need2 - n_min) * cost2))
        ans = min(ans, n_max * costBoth)
        
        return ans

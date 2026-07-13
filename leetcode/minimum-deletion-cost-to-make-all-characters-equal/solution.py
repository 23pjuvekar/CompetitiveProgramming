class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        cost_of_letters = defaultdict(int)
        total = 0
        for i in range(len(s)):
            cost_of_letters[s[i]] += cost[i]
            total += cost[i]
        res = float("inf")
        for _, amt in cost_of_letters.items():
            res = min(res, total - amt)
        return res

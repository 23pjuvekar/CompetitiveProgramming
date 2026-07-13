class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a = 0
        b = 0
        c = 0 
        for i in range(n):
            current_step_cost = costs[i]
            cost_i = min(c + 1, b + 4, a + 9) + current_step_cost
            a = b
            b = c
            c = cost_i
        return c

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:

        answer = []
        m = cost[0]
        for c in cost:
            m = min(c, m)
            answer.append(m)
        return answer

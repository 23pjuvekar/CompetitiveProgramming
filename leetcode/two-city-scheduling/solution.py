class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        h = []
        n = len(costs)
        res = 0

        for a, b in costs:
            heappush(h, [-abs(a - b), a, b])

        a_c = 0
        b_c = 0

        while h:
            d, a, b = heappop(h)
            if a_c == n // 2:
                res += b
            elif b_c == n // 2:
                res += a
            else:
                if a > b:
                    res += b
                    b_c += 1
                else:
                    res += a
                    a_c += 1
        return res

class Solution:
    def fillCups(self, amount: List[int]) -> int:

        h = []
        res = 0

        for amt in amount:
            if amt != 0:
                h.append(-amt)
        
        heapify(h)
        
        while h:
            v1 = -heappop(h)
            if h:
                v2 = -heappop(h)
                if v2 - 1 > 0:
                    heappush(h, -(v2 - 1))
            if v1 - 1 > 0:
                heappush(h, -(v1 - 1))
            res += 1
        
        return res

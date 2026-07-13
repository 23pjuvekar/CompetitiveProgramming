class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        heap = []
        heapify(heap)

        for c in cost:
            heappush(heap, -c)
        
        count = 0
        res = 0
        while heap:
            val = -heappop(heap)
            count += 1
            if count % 3 != 0:
                res += val
        return res

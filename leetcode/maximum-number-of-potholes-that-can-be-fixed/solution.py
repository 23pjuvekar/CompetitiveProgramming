class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        length = 0
        heap = []
        heapq.heapify(heap)

        for r in road:
            if r == ".":
                if length != 0:
                    heapq.heappush(heap, -length)
                length = 0
            elif r == "x":
                length += 1
            
        if length != 0:
            heapq.heappush(heap, -length)

        res = 0
        budget_rem = budget
        
        while heap and budget_rem != 0:
            val = -heapq.heappop(heap)
            if budget_rem >= val + 1:
                res += val
                budget_rem -= (val + 1)
            else:
                res += (budget_rem - 1)
                budget_rem = 0
        
        return res

class Solution:
    def largestInteger(self, num: int) -> int:

        odd_heap = []
        even_heap = []
        res = ""

        for c in str(num):
            if int(c) % 2 == 0:
                heapq.heappush(even_heap, -int(c))
            else:
                heapq.heappush(odd_heap, -int(c))
            
        for c in str(num):
            if int(c) % 2 == 0:
                res += str(-heapq.heappop(even_heap))
            else:
                res += str(-heapq.heappop(odd_heap))

        return int(res)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        min_heap = []
        heapq.heapify(min_heap)

        for interval in intervals:
            heapq.heappush(min_heap, [interval[0], 1])
            heapq.heappush(min_heap, [interval[1], -1])

        curr = 0
        res = 0
        while min_heap:
            element = heapq.heappop(min_heap)
            curr += element[1]
            res = max(res, curr)
        
        return res

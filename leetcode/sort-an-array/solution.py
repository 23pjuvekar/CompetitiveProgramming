class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        heap = []
        heapq.heapify(heap)

        for num in nums:
            heapq.heappush(heap, num)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap))
        
        return res

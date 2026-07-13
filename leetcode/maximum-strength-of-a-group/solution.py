class Solution:
    def maxStrength(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        neg_heap = []
        heapq.heapify(neg_heap)
        res = 0

        for num in nums:
            if num > 0:
                if res == 0:
                    res = 1
                res *= num
            elif num < 0:
                heapq.heappush(neg_heap, num)
            
        
        while len(neg_heap) > 1:
            if res == 0:
                res = 1
            res *= neg_heap[0]
            heapq.heappop(neg_heap)
            res *= neg_heap[0]
            heapq.heappop(neg_heap)
        
        return res

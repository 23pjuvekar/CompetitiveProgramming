class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        heap = []
        res = [0] * len(nums)
        heapq.heapify(heap)

        for i in range(len(nums)):
            heapq.heappush(heap, [nums[i], i])

        while k > 0:
            item = heapq.heappop(heap)
            item[0] = item[0] * multiplier
            heapq.heappush(heap, item)
            k -=1

        for item in heap:
            res[item[1]] = item[0]
        
        return res

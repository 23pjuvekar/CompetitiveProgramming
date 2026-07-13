class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        heap = []
        heapq.heapify(heap)

        for num in nums:
            heapq.heappush(heap, num)
        
        i = 0
        while heap:
            nums[i] = heapq.heappop(heap)
            i += 1
            
        return nums

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        heapify(nums)
        while k:
            val = heappop(nums)
            heappush(nums, -val)
            k -= 1
        return sum(nums)

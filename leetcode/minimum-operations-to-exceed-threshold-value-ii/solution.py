class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        res = 0

        while nums[0] < k:
            x = nums[0]
            heapq.heappop(nums)
            y = nums[0]
            heapq.heappop(nums)
            add_val = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, add_val)
            res += 1
        
        return res

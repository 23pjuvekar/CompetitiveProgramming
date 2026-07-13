class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)
        res = 0
        for i in range(k):
            val = heappop(nums)
            res -= val
            heappush(nums, -ceil(-val / 3))
        return res

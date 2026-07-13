class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:

        res = float("-inf")
        n = len(nums)
        smallest = float("inf")
        largest = float("-inf")
        for j in range(m - 1, n):
            i = j - m + 1
            smallest = min(smallest, nums[i])
            largest = max(largest, nums[i])
            res = max(res, nums[j] * smallest, nums[j] * largest)
        return res

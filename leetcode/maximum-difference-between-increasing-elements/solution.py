class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        smallest = nums[0]
        res = 0
        for num in nums:
            res = max(res, num - smallest)
            smallest = min(smallest, num)
        if res == 0:
            return -1
        return res

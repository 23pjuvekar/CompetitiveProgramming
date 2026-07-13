class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        post = sum(nums)
        pre = 0

        for i in range(len(nums)):
            post -= nums[i]
            if pre == post:
                return i
            pre += nums[i]
        return -1

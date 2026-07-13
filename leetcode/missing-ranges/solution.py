class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """


        nums = [lower-1] + nums + [upper+1]
    
        res = []

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                res.append([nums[i-1] + 1, nums[i] - 1])
        return res

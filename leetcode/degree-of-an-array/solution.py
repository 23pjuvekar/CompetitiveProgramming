class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        values = {}
        max_length = 1

        for i in range(len(nums)):
            if nums[i] not in values:
                values[nums[i]] = [1, i, i]
            else:
                values[nums[i]][0] += 1
                values[nums[i]][2] = i
                max_length = max(max_length, values[nums[i]][0])
        
        res = len(nums)
        for key, val in values.items():
            if val[0] == max_length:
                res = min(res, val[2] - val[1] + 1)
        return res

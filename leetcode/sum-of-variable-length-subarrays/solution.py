class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        prefix = []
        res = 0
        prev = 0

        for num in nums:
            prefix.append(prev + num)
            prev += num

        for i in range(len(nums)):
            start = max(0, i - nums[i]) - 1
            if start == -1:
                res += (prefix[i])
            else:
                res += (prefix[i] - prefix[start])
        
        return res

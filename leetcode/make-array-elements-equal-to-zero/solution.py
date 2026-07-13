class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prev = 0
        end = sum(nums)
        res = 0
        for i in range(len(nums)):
            prev += nums[i]
            end -= nums[i]
            if nums[i] == 0 and abs(prev - end) < 2:
                res += 1
                if abs(prev - end) == 0:
                    res += 1
        return res

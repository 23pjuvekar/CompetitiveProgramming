class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        start = min(nums)
        end = len(nums) + start
        nums = set(nums)

        for number in range(start, end):
            if number not in nums:
                return False
        return True

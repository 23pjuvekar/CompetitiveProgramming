class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:

        average = (sum(nums) // len(nums)) + 1
        nums = set(nums)

        while average in nums or average < 1:
            average += 1
        return average

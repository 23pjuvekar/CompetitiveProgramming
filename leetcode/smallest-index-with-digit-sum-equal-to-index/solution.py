class Solution:
    def smallestIndex(self, nums: List[int]) -> int:


        for i in range(len(nums)):
            num = nums[i]
            total = 0
            for c in str(num):
                total += int(c)
            if i == total:
                return i
        return -1

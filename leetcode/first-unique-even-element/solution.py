class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        count = Counter(nums)

        for num in nums:
            if num % 2 == 0 and count[num] == 1:
                return num
        return -1

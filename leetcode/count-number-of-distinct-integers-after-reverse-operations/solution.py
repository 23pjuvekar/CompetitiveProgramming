class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        values = set(nums)

        for num in nums:
            values.add(int(str(num)[::-1]))
        return len(values)

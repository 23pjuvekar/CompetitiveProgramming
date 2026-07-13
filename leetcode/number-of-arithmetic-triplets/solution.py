class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        nums = set(nums)
        res = 0
        for num in nums:
            if num + diff in nums and num + diff + diff in nums:
                res += 1
        return res

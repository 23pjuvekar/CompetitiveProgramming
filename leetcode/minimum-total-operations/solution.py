class Solution:
    def minOperations(self, nums: List[int]) -> int:

        operations = 0
        last = nums[-1]
        for num in nums[::-1]:
            if num != last:
                operations += 1
                last = num
        return operations

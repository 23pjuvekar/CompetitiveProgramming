class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        overall_gcd = numsDivide[0]
        for value in numsDivide[1:]:
            overall_gcd = gcd(overall_gcd, value)

        sorted_nums = sorted(nums)
        deletions = 0
        for value in sorted_nums:
            if overall_gcd % value == 0:
                return deletions
            deletions += 1

        return -1

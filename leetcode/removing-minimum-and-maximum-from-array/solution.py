class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        ma = max(nums)
        mi = min(nums)
        ia = 0
        ii = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == ma:
                ia = i
            if nums[i] == mi:
                ii = i
        return min((n - ii) + (ia + 1), (n - ia) + (ii + 1), max(ia + 1, ii + 1), max(n - ii, n - ia))

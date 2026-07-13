class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        n = len(nums)
        ma = [0] * n
        ma[0] = nums[0]
        for i in range(1, n):
            ma[i] = max(ma[i - 1], nums[i])
        mi = [0] * n
        mi[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            mi[i] = min(mi[i + 1], nums[i])
        for i in range(n):
            if ma[i] - mi[i] <= k:
                return i
        return -1

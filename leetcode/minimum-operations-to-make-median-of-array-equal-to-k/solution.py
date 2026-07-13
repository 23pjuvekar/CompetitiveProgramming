class Solution:
    def minOperationsToMakeMedianK(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mid = n // 2

        ops = 0

        if nums[mid] < k:
            for i in range(mid, n):
                if nums[i] < k:
                    ops += k - nums[i]
                else:
                    break
        elif nums[mid] > k:
            for i in range(mid, -1, -1):
                if nums[i] > k:
                    ops += nums[i] - k
                else:
                    break

        return ops

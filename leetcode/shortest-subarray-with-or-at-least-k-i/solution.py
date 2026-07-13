class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        l = 0
        res = float('inf')
        total = 0

        for r in range(len(nums)):
            total |= nums[r]

            while total >= k and l <= r:
                res = min(res, r - l + 1)

                # Recalculate total for the new window
                l += 1
                total = 0
                for i in range(l, r + 1):
                    total |= nums[i]

        if res == float('inf'):
            return -1
        return res

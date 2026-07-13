class Solution:
    def maxNonDecreasingLength(self, nums1, nums2):
        memo = {}

        def dp(i, prev):
            if (i, prev) in memo:
                return memo[(i, prev)]

            if i == len(nums1):
                return 0

            res = 0
            if prev == 0:
                res = dp(i + 1, prev)

            if prev <= nums1[i]:
                res = max(res, 1 + dp(i + 1, nums1[i]))
            if prev <= nums2[i]:
                res = max(res, 1 + dp(i + 1, nums2[i]))

            memo[(i, prev)] = res
            return res

        return dp(0, 0)

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0

        # target in the array
        m = defaultdict(int)
        l = 0
        r = 0
        for x in nums:
            while r < n and nums[r] <= x + k:
                m[nums[r]] += 1
                r += 1
            while l < n and nums[l] < x - k:
                m[nums[l]] -= 1
                l += 1
            mx_ops = r - l - m[x]
            res = max(res, min(mx_ops, numOperations) + m[x])

        # target not in arr
        l = 0
        for r in range(n):
            while l < n and nums[l] + (k * 2) < nums[r]:
                l += 1
            mx_ops = r - l + 1
            res = max(res, min(mx_ops, numOperations))

        return res
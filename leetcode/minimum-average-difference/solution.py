class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        n = len(nums)
        prev = 0
        end = sum(nums)
        p = 0
        e = n
        res = 0
        t = float('inf')
        for i in range(n):
            prev += nums[i]
            end -= nums[i]
            p += 1
            e -= 1
            if e == 0:
                e = 1
            if t > abs(prev // p - end // e):
                t = abs(prev // p - end // e)
                res = i
        return res

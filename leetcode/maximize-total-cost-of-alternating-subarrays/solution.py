class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def f(idx, sign):
            if idx == n:
                return 0
            if (idx, sign) in memo:
                return memo[(idx, sign)]
            val = nums[idx] if sign == 0 else -nums[idx]
            p1 = val + f(idx + 1, 1 - sign)
            p2 = nums[idx] + f(idx + 1, 1)
            res = max(p1, p2)
            memo[(idx, sign)] = res
            return res

        return f(0, 0)

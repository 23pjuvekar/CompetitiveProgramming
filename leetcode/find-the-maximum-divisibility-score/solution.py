class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:

        res = min(divisors)
        m = 0

        for d in divisors:
            curr = 0
            for num in nums:
                if num % d == 0:
                    curr += 1
            if curr == m:
                res = min(res, d)
            elif curr > m:
                res = d
                m = curr
        return res

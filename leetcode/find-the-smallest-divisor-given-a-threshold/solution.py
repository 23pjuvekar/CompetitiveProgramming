class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def test(n):
            res = 0
            for num in nums:
                res += ceil(num / n)
            return res

        l = 1
        r = max(nums)
        
        while l < r:
            m = (l + r) // 2
            if test(m) <= threshold:
                r = m
            else:
                l = m + 1
                
        return r

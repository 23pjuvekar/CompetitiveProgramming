class Solution:
    def minimumK(self, nums: List[int]) -> int:

        def nonPositive(k):
            return sum(math.ceil(num / k) for num in nums)
        
        l, r = 1, max(max(nums), len(nums))
        while l < r:
            m = (l + r) // 2
            if nonPositive(m) <= m * m:
                r = m
            else:
                l = m + 1

        return l

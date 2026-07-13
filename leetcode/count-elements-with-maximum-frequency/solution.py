class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m = 0
        res = 0
        for k, a in Counter(nums).items():
            if a > m:
                res = a
                m = a
            elif a == m:
                res += a
        return res

class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        seen = set()
        res = -1

        for num in nums:
            if -(num) in seen:
                res = max(abs(num), res)
            seen.add(num)
        return res

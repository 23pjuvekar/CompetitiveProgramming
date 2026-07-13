class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:

        res = set()
        for n, t in zip(nums, target):
            if n != t:
                res.add(n)
        return len(res)

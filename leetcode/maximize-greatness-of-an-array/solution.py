class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for a in nums:
            if a > nums[res]:
                res += 1
        return res

class Solution:
    def scoreDifference(self, nums: List[int]) -> int:

        p1 = 0
        p2 = 0
        p1_actice = True

        for i in range(len(nums)):
            if i % 6 == 5:
                p1_actice = not p1_actice
            if nums[i] % 2 == 1:
                p1_actice = not p1_actice
            if p1_actice:
                p1 += nums[i]
            else:
                p2 += nums[i]
        return p1 - p2

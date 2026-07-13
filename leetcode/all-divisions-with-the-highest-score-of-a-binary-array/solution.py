class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        l = 0
        r = sum(nums)
        res = [0]
        t = l + r
        for i in range(len(nums)):
            if nums[i] == 0:
                l += 1
            else:
                r -= 1
            if t < l + r:
                t = l + r
                res = [i+1]
            elif t == l + r:
                res.append(i+1)
        return res

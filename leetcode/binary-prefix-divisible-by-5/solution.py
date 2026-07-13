class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        curr = 0
        res = []
        for n in nums:
            curr *= 2
            curr += n
            if curr % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res

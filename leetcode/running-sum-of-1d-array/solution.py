class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        res = []
        prev = 0

        for num in nums:
            res.append(num + prev)
            prev = num + prev

        return res

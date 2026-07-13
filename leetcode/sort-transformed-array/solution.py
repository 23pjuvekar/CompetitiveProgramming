class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        res = []

        for i in range(len(nums)):
            num = nums[i]
            res.append((a * num * num) + (b * num) + c)
        
        res.sort()

        return res

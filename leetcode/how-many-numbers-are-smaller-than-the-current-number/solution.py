class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}
        for i, v in enumerate(temp):
            if v not in d:
                d[v] = i
        arr = []
        for i in nums:
            arr.append(d[i])
        return arr

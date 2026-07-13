class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        mp = {}
        for i in range(len(nums)):
            num = nums[i]
            mp[num] = i
        for x, y in operations:
            mp[y] = mp[x]
            del mp[x]
        res = [0] * len(nums)
        for k, v in mp.items():
            res[v] = k
        return res

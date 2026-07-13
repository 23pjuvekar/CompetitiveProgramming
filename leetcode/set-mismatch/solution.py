class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        value = Counter(nums)
        res = [-1, -1]
        for i in range(1, len(nums) + 1):
            if i not in value:
                res[1] = i
            if value[i] == 2:
                res[0] = i
        return res

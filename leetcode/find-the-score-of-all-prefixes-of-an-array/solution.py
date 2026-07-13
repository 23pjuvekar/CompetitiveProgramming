class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:

        m = nums[0]
        res = [2 * nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            m = max(m, num)
            res.append(res[i-1] + num + m)
        return res

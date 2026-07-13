class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:


        nums.sort()
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            nums[i] = curr
        res = []
        for q in queries:
            res.append(bisect_right(nums, q))
        return res

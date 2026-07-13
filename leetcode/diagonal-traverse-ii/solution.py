class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:


        values = defaultdict(list)
        start = float("inf")
        end = float("-inf")
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                values[r + c].append([c, nums[r][c]])
                start = min(start, r + c)
                end = max(end, r + c)
        res = []
        for v in range(start, end + 1):
            values[v].sort()
            res.extend([value for index, value in values[v]])
        return res

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:


        groups = []
        map_groups = {}

        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(n)
            map_groups[n] = len(groups) - 1 
        
        res = []
        for n in nums:
            res.append(groups[map_groups[n]].popleft())
        return res

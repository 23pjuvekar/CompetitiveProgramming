class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        count = Counter(nums)

        res = 0
        for key, val in count.items():
            possible_count = val
            if key + 1 in count:
                res = max(res, val + count[key + 1])
            if key - 1 in count:
                res = max(res, val + count[key - 1])
        return res

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        c1 = defaultdict(int)
        n = len(nums)

        for l in nums:
            for num in l:
                c1[num] += 1
        res = []
        for key, val in c1.items():
            if val == n:
                res.append(key)
        res.sort()
        return res

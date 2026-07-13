class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        mp = defaultdict(list)
        res = [0] * len(nums)
        for i in range(len(nums)):
            mp[nums[i]].append(i)
        for k, l in mp.items():
            curr = 0
            total = sum(l)
            n = len(l)
            for j in range(n):
                v = l[j]
                res[v] = total - ((n - j) * v) + ((j) * v) - curr
                curr += v
                total -= v
        return res

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        c = Counter(nums)
        res = 0
        for key, val in c.items():
            res += (val * c[key + k])
            res += (val * c[key - k])
        return res // 2

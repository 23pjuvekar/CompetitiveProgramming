class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        for key, val in Counter(nums).items():
            if val % 2 == 1:
                res[1] += 1
            res[0] += val // 2
        return res

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:

        res = 0
        for key, val in Counter(nums).items():
            if val % k == 0:
                res += key * val
        return res

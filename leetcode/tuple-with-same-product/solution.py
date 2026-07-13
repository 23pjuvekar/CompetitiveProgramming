class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        counts = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                counts[nums[i] * nums[j]] += 1
        res = 0
        for val in counts.values():
            res += val * (val - 1) * 4
        return res

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        unique_vals = sorted(counts.keys(), reverse=True)
        res = 0
        ops = 0
        for i in range(len(unique_vals) - 1):
            ops += counts[unique_vals[i]]
            res += ops
            
        return res

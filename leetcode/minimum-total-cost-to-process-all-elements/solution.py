class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        total = sum(nums)
        operations_ceiling = math.ceil(total / k)
        return (operations_ceiling - 1) * operations_ceiling // 2 % MOD

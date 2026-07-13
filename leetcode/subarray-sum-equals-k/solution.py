class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        total = 0
        prefix_map = {0 : 1}

        for num in nums:
            total += num
            needed = total - k
            
            res += prefix_map.get(needed, 0)
            prefix_map[total] = 1 + prefix_map.get(total, 0)

        return res

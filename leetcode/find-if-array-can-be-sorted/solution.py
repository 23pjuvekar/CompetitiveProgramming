class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def count_set_bits(n):
            return bin(n).count('1')
        prev_max = -float('inf')
        curr_min = nums[0]
        curr_max = nums[0]
        prev_bits = count_set_bits(nums[0])
        for x in nums:
            bits = count_set_bits(x)
            if bits == prev_bits:
                curr_min = min(curr_min, x)
                curr_max = max(curr_max, x)
            else:
                if curr_min < prev_max:
                    return False
                prev_max = curr_max
                curr_min = x
                curr_max = x
                prev_bits = bits
        
        return curr_min >= prev_max

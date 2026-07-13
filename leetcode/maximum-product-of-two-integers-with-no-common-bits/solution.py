class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = max(nums)
        bits = max_num.bit_length()
        if bits == 0:
            return 0
        size = 1 << bits
        full_mask = size - 1

        best_subset = [0] * size
        for val in nums:
            best_subset[val] = val

        for b in range(bits):
            step = 1 << b
            for m in range(size):
                if m & step:
                    without = m ^ step
                    if best_subset[without] > best_subset[m]:
                        best_subset[m] = best_subset[without]

        ans = 0
        for a in nums:
            comp = full_mask ^ a
            b = best_subset[comp]
            if b:
                ans = max(ans, a * b)

        return ans

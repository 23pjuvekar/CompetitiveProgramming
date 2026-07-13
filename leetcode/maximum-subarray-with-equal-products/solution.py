class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def lcm(a, b):
            return (a * b) // gcd(a, b) if a and b else 0

        n = len(nums)
        if n == 0:
            return 0
        
        max_len = 1

        for start in range(n):
            gcd_val = nums[start]
            lcm_val = nums[start]
            prod_val = nums[start]

            if prod_val == gcd_val * lcm_val:
                max_len = max(max_len, 1)

            for end in range(start + 1, n):
                gcd_val = gcd(gcd_val, nums[end])
                lcm_val = lcm(lcm_val, nums[end])
                prod_val *= nums[end]

                if prod_val == gcd_val * lcm_val:
                    curr_len = end - start + 1
                    max_len = max(max_len, curr_len)

        return max_len

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums1 = 0
        gcd_value = 0

        for num in nums:
            if num == 1:
                nums1 += 1
            gcd_value = gcd(gcd_value, num)

        if nums1 > 0:
            return n - nums1
        
        if gcd_value > 1:
            return -1
        
        min_length = n
        for i in range(n):
            gcd_value = 0
            for j in range(i, n):
                gcd_value = gcd(gcd_value, nums[j])
                if gcd_value == 1:
                    min_length = min(min_length, j - i + 1)
                    break
        
        return min_length - 1 + n - 1

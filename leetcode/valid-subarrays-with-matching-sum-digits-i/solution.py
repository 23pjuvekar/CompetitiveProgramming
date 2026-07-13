class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:

        n = len(nums)
        count = 0
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                
                s = str(current_sum)
                first_digit = int(s[0])
                last_digit = int(s[-1])
                
                if first_digit == x and last_digit == x:
                    count += 1
                    
        return count

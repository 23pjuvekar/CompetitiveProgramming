class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        total_zeros = s.count('0')
        
        ones = 0
        zeros = total_zeros
        result = total_zeros
        
        for c in s:
            if c == '1':
                ones += 1
            else:
                zeros -= 1
            
            result = min(result, ones + zeros)
        
        return result

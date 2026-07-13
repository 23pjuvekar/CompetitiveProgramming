class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0 
        needed_right = 0
        i = 0
        
        while i < len(s):
            if s[i] == '(':
                needed_right += 2
            else:
                if i + 1 < len(s) and s[i+1] == ')':
                    needed_right -= 2
                    i += 1
                else:
                    res += 1
                    needed_right -= 2
                if needed_right < 0:
                    res += 1
                    needed_right += 2
            
            i += 1
            
        return res + needed_right

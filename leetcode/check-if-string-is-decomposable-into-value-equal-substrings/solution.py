class Solution:
    def isDecomposable(self, s: str) -> bool:
        found_two = False
        i = 0
        n = len(s)
        
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            length = j - i
            
            if length % 3 == 0:
                pass
            elif length % 3 == 2 and not found_two:
                found_two = True
            else:
                return False
            
            i = j
        
        return found_two

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:

        c1 = 0
        c2 = 0
        cp = 0

        for c in text:
            if c == pattern[1]:
                c2 += 1
                cp += c1
            if c == pattern[0]:
                c1 += 1
            
        
        return cp + max(c1, c2)

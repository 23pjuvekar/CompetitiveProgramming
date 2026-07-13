class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        p = 0

        for c in s:
            if p == len(t):
                return False
            while c != t[p]:
                p += 1
                if p == len(t):
                    return False
            p += 1
        
        return True

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        o = -1
        t = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if o == -1:
                    o = i
                elif t == -1:
                    t = i
                else:
                    return False
        
        return s1[o] == s2[t] and s1[t] == s2[o]

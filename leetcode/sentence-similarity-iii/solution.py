class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        # s1 is always the smaller one
        if len(s1) > len(s2):
            s1, s2 = s2, s1


        l = 0
        while l < len(s1) and s1[l] == s2[l]:
            l += 1
        
        if l == len(s1):
            return True
        
        r = 0
        while r < len(s1) and s1[len(s1) - (r + 1)] == s2[len(s2) - (r + 1)]:
            r += 1
        
        if r == len(s1):
            return True

        if l + r + 1 > len(s1):
            return True
    
        return False

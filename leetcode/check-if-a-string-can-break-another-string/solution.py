class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        s1_l = list(s1)
        s1_l.sort()
        s2_l = list(s2)
        s2_l.sort()
        
        score = 0
        target = len(s1)
        for c1, c2 in zip(s1_l, s2_l):
            if c1 == c2:
                target -= 1
            elif c1 > c2:
                score -= 1
            else:
                score += 1
        return abs(score) == target

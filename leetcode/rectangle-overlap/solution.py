class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        A, B, C, D = rec1[0], rec1[1], rec1[2], rec1[3]
        E, F, G, H = rec2[0], rec2[1], rec2[2], rec2[3]
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        if x1 < x2 and y1 < y2:
            return True
        return False

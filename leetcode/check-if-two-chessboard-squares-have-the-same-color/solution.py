class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

        c1_black = True
        c2_black = True

        if (1 + ord(coordinate1[0]) - ord("a") + int(coordinate1[1])) % 2 != 0:
            c1_black = False
        
        if (1 + ord(coordinate2[0]) - ord("a") + int(coordinate2[1])) % 2 != 0:
            c2_black = False
        
        return c1_black == c2_black

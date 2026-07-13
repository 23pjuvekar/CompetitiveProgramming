class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res = []

        for i in range(len(s)):
            cy, cx = startPos
            l = 0
            for c in s[i:]:
                if c == "R":
                    cx += 1
                elif c == "L":
                    cx -= 1
                elif c == "U":
                    cy -= 1
                elif c == "D":
                    cy += 1
                if cx < 0 or cx > n - 1 or cy < 0 or cy > n - 1:
                    break
                l += 1
            res.append(l)
        return res

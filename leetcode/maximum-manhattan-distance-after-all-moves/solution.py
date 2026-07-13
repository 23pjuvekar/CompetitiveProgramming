class Solution:
    def maxDistance(self, moves: str) -> int:

        positions = [0, 0, 0, 0, 0] # U, D, L, R, _
        for c in moves:
            if c == "U":
                positions[0] += 1
            elif c == "D":
                positions[1] += 1
            elif c == "L":
                positions[2] += 1
            elif c == "R":
                positions[3] += 1
            elif c == "_":
                positions[4] += 1
        
        return positions[4] + abs(positions[0] - positions[1]) + abs(positions[2] - positions[3])

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        d = 0
        for i in instructions:
            if i == 'G':
                x += dirs[d][0]
                y += dirs[d][1]
            elif i == 'L':
                d = (d - 1) % 4
            elif i == 'R':
                d = (d + 1) % 4

        return (x == 0 and y == 0) or (d != 0)

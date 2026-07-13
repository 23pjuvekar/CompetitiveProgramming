class Solution:
    def isPathCrossing(self, path: str) -> bool:

        past_pos = set()
        pos = (0, 0)
        past_pos.add(pos)
        
        for direction in path:
            if direction == "N":
                new_pos = (pos[0] + 1, pos[1])
            elif direction == "E":
                new_pos = (pos[0], pos[1] + 1)
            elif direction == "S":
                new_pos = (pos[0] - 1, pos[1])
            elif direction == "W":
                new_pos = (pos[0], pos[1] - 1)
            
            if new_pos in past_pos:
                return True
            past_pos.add(new_pos)
            pos = new_pos
        return False

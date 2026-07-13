class Solution(object):
    def escapeGhosts(self, ghosts, target):
        def manhattan(source, dest):
            return abs(source[0] - dest[0]) + abs(source[1] - dest[1])
        origin = [0, 0]
        return all(manhattan(origin, target) < manhattan(ghost, target)
                   for ghost in ghosts)

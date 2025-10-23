class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        q = deque()
        q.append((0, 0))
        visited = set()
        possible = [[2, 1], [1, 2], [-1, 2], [2, -1], [-2, 1], [1, -2], [-2, -1], [-1, -2]]
        res = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) == (x, y):
                    return res
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for nr, nc in possible:
                    if (nr + r, nc + c) not in visited:
                        q.append((nr + r, nc + c))
            res += 1
        


        
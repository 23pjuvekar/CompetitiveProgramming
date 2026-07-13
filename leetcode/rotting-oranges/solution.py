class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def add(r, c):
            if (r not in range(ROWS)) or (c not in range(COLS)) or ((r, c) in visited) or (grid[r][c] == 0):
                return
            q.append([r, c])
            visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r, c))

        count = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            count += 1
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        if count != 0:
            return count - 1
        return count

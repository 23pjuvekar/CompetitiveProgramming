class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        
        def neighbors(r, c, visited):
            for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if (0 <= nr < R and 0 <= nc < C and 
                    (nr,nc) not in visited and grid[nr][nc]):
                    yield (nr, nc)
        
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    q = deque([((r,c), grid[r][c], {(r,c)})])
                    while q:
                        pos, val, visited = q.popleft()
                        res = max(res, val)
                        for nr, nc in neighbors(*pos, visited):
                            new_visited = visited | {(nr,nc)}
                            q.append(((nr,nc), val + grid[nr][nc], new_visited))
        return res

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        R = len(isWater)
        C = len(isWater[0])
        q = deque()
        res = [[-1] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if isWater[r][c]:
                    q.append((r, c))
                    res[r][c] = 0

        while q:
            r, c = q.popleft()
            h = res[r][c]
            neighbors = [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nr, nc in neighbors:
                if nr < 0 or nc < 0 or nr == R or nc == C or res[nr][nc] != -1:
                    continue
                q.append((nr, nc))
                res[nr][nc] = h + 1
        
        return res

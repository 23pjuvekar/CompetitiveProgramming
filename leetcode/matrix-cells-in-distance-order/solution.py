class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        q = deque()
        q.append([rCenter, cCenter])
        res = []
        seen = set()
        while q:
            r, c = q.popleft()
            if (r, c) not in seen:
                res.append([r, c])
                seen.add((r, c))
                cords = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
                for nr, nc in cords:
                    if (nr, nc) not in seen and 0 <= nr < rows and 0 <= nc < cols:
                        q.append([nr, nc]) 
        return res

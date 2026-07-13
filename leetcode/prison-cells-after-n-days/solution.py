class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        m = len(cells)
        n = ((n -1) % 14) + 1
        for _ in range(n):
            new = [0] * m
            for i in range(1, m - 1):
                if cells[i-1] == cells[i+1]:
                    new[i] = 1
                else:
                    new[i] = 0
            cells = new

        return cells

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        rows = len(land)
        cols = len(land[0])
        result = []

        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1:
                    is_top_left = True
                    if r > 0 and land[r - 1][c] == 1:
                        is_top_left = False
                    if c > 0 and land[r][c - 1] == 1:
                        is_top_left = False

                    if is_top_left:
                        r2 = r
                        c2 = c
                        
                        while c2 + 1 < cols and land[r][c2 + 1] == 1:
                            c2 += 1
                        
                        while r2 + 1 < rows and land[r2 + 1][c] == 1:
                            r2 += 1
                        
                        result.append([r, c, r2, c2])

        return result

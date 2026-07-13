class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        def count_color(r, c):
            W_C = 0
            B_C = 0
            values = [[0, 0], [0, 1], [1, 0], [1, 1]]

            for value in values:
                if grid[r + value[0]][c + value[1]] == "W":
                    W_C += 1
                elif grid[r + value[0]][c + value[1]] == "B":
                    B_C += 1
                
            if B_C == 2 or W_C == 2:
                return False
            return True
        
        return count_color(0, 0) or count_color(0, 1) or count_color(1, 0) or count_color(1, 1)

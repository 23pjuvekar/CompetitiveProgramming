class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orginal_color = image[sr][sc]
        ROWS = len(image)
        COLS = len(image[0])
        visited = set()

        def dfs(x, y):

            if x < 0 or x == ROWS or y < 0 or y == COLS or image[x][y] != orginal_color or (x, y) in visited:
                return

            image[x][y] = color
            visited.add((x, y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        
        dfs(sr, sc)

        return image

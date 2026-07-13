class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        
        def build(n, offset):
            if n == 0:
                return [[offset]]
            half = 2 ** (n - 1)
            quarter = half * half
            tr = build(n - 1, offset)
            br = build(n - 1, offset + quarter)
            bl = build(n - 1, offset + 2 * quarter)
            tl = build(n - 1, offset + 3 * quarter)
            grid = []
            for i in range(half):
                grid.append(tl[i] + tr[i])
            for i in range(half):
                grid.append(bl[i] + br[i])
            return grid

        return build(n, 0)

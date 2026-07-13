class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:


        def above(y_line):
            res = 0
            for x, y, l in squares:
                if y + l <= y_line:
                    res += l * l
                elif y >= y_line:
                    res -= l * l
                else:
                    below_line = y_line - y
                    above_line = l - below_line
                    res += below_line * l
                    res -= above_line * l
            return res

        l = 0
        r = 2 * 10**9

        while r - l > 10 ** (-5):
            m = (r + l) / 2
            if above(m) >= 0:
                r = m
            else:
                l = m
        return m

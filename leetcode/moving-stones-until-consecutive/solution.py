class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:

        a, b, c = sorted([a, b, c])
        if a + 1 == b == c - 1:
            min_steps = 0
        elif b - a > 2 and c - b > 2:
            min_steps = 2
        else:
            min_steps = 1
        max_steps = c - a - 2
        return [min_steps, max_steps]

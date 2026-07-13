class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        m1 = 0
        m2 = 0
        res = 0
        for s1, s2 in zip(player1, player2):
            if m1 > 0:
                res += 2 * s1
                m1 -= 1
            else:
                res += s1
            if m2 > 0:
                res -= 2 * s2
                m2 -= 1
            else:
                res -= s2
            if s1 == 10:
                m1 = 2
            if s2 == 10:
                m2 = 2

        if res == 0:
            return 0
        if res > 0:
            return 1
        return 2

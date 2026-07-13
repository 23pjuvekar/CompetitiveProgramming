# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
# 1, 2, 3, 4, 3, 2, 1, 2, 3, 4,  3,  2,  1,

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        mod = n -1
        reverse = (time // mod) % 2
        offset = time % mod

        if reverse == 1:
            return n - offset
        else:
            return 1 + offset

class Solution:
    def countTime(self, time: str) -> int:

        t1 = time[:2]
        t2 = time[3:]
        res = 0
        if t1 == "??":
            res = 24
        else:
            if t1[0] == "?":
                res = 3
                if int(t1[1]) > 3:
                    res -= 1
            elif t1[1] == "?":
                if int(t1[0]) == 2:
                    res = 4
                else:
                    res = 10
            else:
                res = 1

        if t2 == "??":
            res *= 60
        else:
            if t2[0] == "?":
                res *= 6
            elif t2[1] == "?":
                res *= 10
        return res

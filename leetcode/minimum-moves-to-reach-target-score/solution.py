class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        res = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target = target // 2
                maxDoubles -= 1
                res += 1
            elif maxDoubles > 0:
                target -= 1
                res += 1
            else:
                res += (target - 1)
                target = 1
        return res

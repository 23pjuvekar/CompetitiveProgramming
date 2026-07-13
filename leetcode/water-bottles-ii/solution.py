class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        empty = 0
        res = 0
        while numBottles or empty >= numExchange:
            if empty >= numExchange:
                empty -= numExchange
                numExchange += 1
                numBottles += 1
            elif numBottles:
                res += numBottles
                empty += numBottles
                numBottles = 0
            else:
                break
        return res

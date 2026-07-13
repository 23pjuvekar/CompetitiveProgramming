class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        """
        def greater_than_one(spread):
            total = 0
            for c in spread:
                if c > 0:
                    total += 1
            return total >= 2
        curr = [a, b, c]
        res = 0
        while greater_than_one(curr):
            curr.sort()
            curr[1] -= 1
            curr[2] -= 1
            res += 1
        return res
        """
        a,b,c = sorted((a,b,c))
        if a+b<c: return a+b
        return (a+b+c)//2

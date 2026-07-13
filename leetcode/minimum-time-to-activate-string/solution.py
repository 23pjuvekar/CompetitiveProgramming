class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(order)
        sub_string = n * (n + 1) //2
        def calculateAmt(t):
            word = list(s)
            for i in range(t + 1):
                word[order[i]] = "*"
            l = 0
            res = 0
            for r in range(len(word)):
                if word[r] == "*":
                    l = r + 1
                else:
                    res += (r - l + 1)
            return sub_string - res

        l = 0
        r = len(order) - 1
        res = -1
        while l <= r:
            m = (l + r) // 2
            if calculateAmt(m) >= k:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

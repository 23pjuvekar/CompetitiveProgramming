class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        b = set(banned)
        total = 0
        res = 0
        for i in range(1, n + 1):
            if i not in b:
                if total + i > maxSum:
                    return res
                res += 1
                total += i
        return res

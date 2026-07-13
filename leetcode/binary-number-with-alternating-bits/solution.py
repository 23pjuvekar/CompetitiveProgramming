class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        last = -1
        while n:
            if n % 2 == last:
                return False
            last = n % 2
            n = n // 2
        return True

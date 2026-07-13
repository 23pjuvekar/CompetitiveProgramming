class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = 0
        res = 1
        for ch in s:
            n = n * 10 + int(ch)
            if n > k:
                res += 1
                n = int(ch)
            if n > k:
                return -1
        return res

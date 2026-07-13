class Solution:
    def countMonobit(self, n: int) -> int:
        res = 0
        while (2 ** res) - 1 <= n:
            res += 1
        return res

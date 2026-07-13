class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        target = [i for i in range(n)]
        res = 0
        while True:
            new_perm = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    new_perm[i] = perm[i // 2]
                else:
                    new_perm[i] = perm[n // 2 + (i - 1) // 2]
            perm = new_perm
            res += 1
            if perm == target:
                return res

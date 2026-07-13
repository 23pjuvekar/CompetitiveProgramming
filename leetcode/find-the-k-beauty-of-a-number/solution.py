class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        n = str(num)
        l = 0
        res = 0
        for r in range(len(n)):
            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                if int(n[l:r+1]) != 0 and num % int(n[l:r+1]) == 0:
                    res += 1
        return res

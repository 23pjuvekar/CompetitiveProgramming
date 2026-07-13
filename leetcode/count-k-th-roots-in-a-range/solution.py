class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1: return r-l+1
        res = 0 
        for i in range(10**5+1):
            if l <= pow(i, k) <= r: res += 1 
            if pow(i, k) > r: break 
        return res

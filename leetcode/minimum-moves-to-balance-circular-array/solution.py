class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)

        if sum(balance) < 0:
            return -1
        if min(balance) >= 0:
            return 0
        
        sink = -1
        for i in range(n):
            if balance[i] < 0:
                sink = i
                break
        
        needed = abs(balance[sink])
        ans = 0

        L = (sink - 1 + n) % n
        R = (sink + 1) % n
        dist = 1

        while needed > 0:
            if balance[L] > 0:
                take = min(needed, balance[L])
                ans += take * dist
                needed -= take
            if needed == 0: break
            if balance[R] > 0:
                take = min(needed, balance[R])
                ans += take * dist
                needed -= take
            L = (L - 1 + n) % n
            R = (R + 1) % n
            dist += 1
            
        return ans

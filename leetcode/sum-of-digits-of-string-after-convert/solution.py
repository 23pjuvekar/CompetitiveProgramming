class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        t1 = ""
        for c in s:
            t1 += str(ord(c) - ord("a") + 1)
        
        for i in range(k):
            if len(t1) == 1:
                return int(t1)
            t1_n = 0
            for c in t1:
                t1_n += int(c)
            t1 = str(t1_n)
        return int(t1)

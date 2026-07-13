class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        
        h = []
        for _, v in Counter(s).items():
            h.append(v)
        h.sort()
        n = len(h)-k
        if n < 0:
            return 0
        return sum(h[:len(h)-k])

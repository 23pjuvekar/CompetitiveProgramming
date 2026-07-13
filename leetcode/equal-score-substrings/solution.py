class Solution:
    def scoreBalance(self, s: str) -> bool:

        total = 0 
        for c in s:
            total += ord(c) - ord("a") + 1
        
        curr_total = 0
        for c in s:
            curr_total += ord(c) - ord("a") + 1
            if total - curr_total == curr_total:
                return True
        return False

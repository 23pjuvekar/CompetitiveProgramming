class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_count = s.count("a")
        b_count = 0
        res = n

        for c in s:
            if c == "a":
                a_count -= 1
            res = min(res, a_count + b_count)
            if c == "b":
                b_count += 1
        
        return res

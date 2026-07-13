class Solution:
    def minimumChairs(self, s: str) -> int:

        chairs = 0
        res = 0
        for c in s:
            if c == "E":
                chairs += 1
            else:
                chairs -= 1
            res = max(res, chairs)
        return res

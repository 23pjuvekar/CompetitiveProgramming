class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        for l in range(ord(s[0]), ord(s[3]) + 1):
            for n in range(int(s[1]), int(s[4]) + 1):
                res.append(chr(l) + str(n))
        return res

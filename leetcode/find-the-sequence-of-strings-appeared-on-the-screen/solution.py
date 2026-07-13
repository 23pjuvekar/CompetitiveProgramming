class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        curr = ""
        for c in target:
            for i in range(ord("a"), ord(c) + 1):
                res.append(curr + chr(i))
            curr += c
        return res

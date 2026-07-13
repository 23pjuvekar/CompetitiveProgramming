class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:

        res = 0
        for e1 in a:
            for e2 in b:
                for e3 in c:
                    if bin(e1 ^ e2 ^ e3).count("1") % 2 == 0:
                        res += 1
        return res

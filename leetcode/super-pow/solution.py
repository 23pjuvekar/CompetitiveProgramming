class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        p = ''
        for i in b:
            p += str(i)
        p = int(p)
        return pow(a, p, 1337)

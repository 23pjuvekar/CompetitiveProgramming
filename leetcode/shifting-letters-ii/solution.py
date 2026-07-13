class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        prefix = [0] * (len(s) + 1)

        for l, r, d in shifts:
            prefix[r + 1] += 1 if d else -1
            prefix[l] += -1 if d else 1

        diff = 0
        res = [ord(c) - ord("a") for c in s]

        for i in reversed(range(len(prefix))):
            diff += prefix[i]
            res[i-1] = (res[i-1] + 26 + diff) % 26
        
        s = [chr(ord("a") + n) for n in res]
        return "".join(s)

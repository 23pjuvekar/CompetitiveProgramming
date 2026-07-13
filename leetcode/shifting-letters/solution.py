class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prev = 0
        for i in range(len(shifts) - 1, -1, -1):
            shifts[i] += prev
            shifts[i] % 26
            prev = shifts[i]
        res = ""
        for i in range(len(s)):
            c = s[i]
            res += chr((ord(c) - ord("a") + shifts[i]) % 26 + ord("a"))
        return res

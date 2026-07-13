class Solution:
    def mirrorFrequency(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for c in "abcdefghijklm01234":
            if c.isdigit():
                mirror = chr(ord('9') - (ord(c) - ord('0')))
            else:
                mirror = chr(ord('z') - (ord(c) - ord('a')))
            if count[c] == 0 and count[mirror] == 0:
                continue
            res += abs(count[c] - count[mirror])
        return res

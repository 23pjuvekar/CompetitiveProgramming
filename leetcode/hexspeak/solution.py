class Solution:
    def toHexspeak(self, num: str) -> str:
        res = ""
        for c in hex(int(num))[2:].upper():
            if c not in {'A', 'B', 'C', 'D', 'E', 'F', '1', '0'}:
                return "ERROR"
            if c == "1":
                res += "I"
            elif c == "0":
                res += "O"
            else:
                res += c
        return res

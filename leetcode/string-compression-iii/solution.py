class Solution:
    def compressedString(self, word: str) -> str:

        res = ""
        last_char = word[0]
        amt = 0
        for w in word:
            if last_char != w:
                if amt != 0:
                    res += str(amt) + last_char
                last_char = w
                amt = 1
            else:
                amt += 1
                if amt == 9:
                    res += str(amt) + last_char
                    amt = 0
        if amt != 0:
            res += str(amt) + last_char
        return res

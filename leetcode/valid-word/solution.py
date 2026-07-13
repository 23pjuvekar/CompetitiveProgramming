class Solution:
    def isValid(self, word: str) -> bool:

        letters = set("qwertyuioplkjhgfdsazxcvbnm")
        vowels = set("aeiou")
        digits = set("0123456789")

        if len(word) < 3:
            return False

        v = False
        o = False

        for c in word:
            if c.lower() not in letters and c.lower() not in digits:
                return False
            if c.lower() in vowels:
                v = True
            if c.lower() in letters and c.lower() not in vowels:
                o = True
        return v and o

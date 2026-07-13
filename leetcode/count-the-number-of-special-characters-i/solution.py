class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        word_values = set(word)
        res = 0


        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in word_values and c.upper() in word_values:
                res += 1
        
        return res

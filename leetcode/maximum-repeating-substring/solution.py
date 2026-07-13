class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:

        res = 0
        w = ""
        while w in sequence:
            res = len(w) // len(word)
            w += word
        return res

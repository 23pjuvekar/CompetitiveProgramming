class Solution:
    def minTimeToType(self, word: str) -> int:

        res = len(word)
        word = "a" + word
        for i in range(len(word) - 1):
            v = abs(ord(word[i + 1]) - ord(word[i])) % 26
            res += min(v, 26 - v)
        return res

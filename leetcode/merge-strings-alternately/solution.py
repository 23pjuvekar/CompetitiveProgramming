class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        length = min(len(word1), len(word2))
        res = ""

        for i in range(length):
            res += word1[i]
            res += word2[i]

        if len(word1) > length:
            res += word1[length:]

        if len(word2) > length:
            res += word2[length:]

        return res

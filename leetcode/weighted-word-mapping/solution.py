class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        key = {}
        for i in range(26):
            key[chr(ord('a') + i)] = weights[i]
        res = ""
        for word in words:
            total = 0
            for c in word:
                total += key[c]
            total = total % 26
            res += chr(ord('z') - total)
        return res

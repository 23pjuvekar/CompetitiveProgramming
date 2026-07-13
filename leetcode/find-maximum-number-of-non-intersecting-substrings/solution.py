class Solution:
    def maxSubstrings(self, word: str) -> int:

        first_map = {}
        res = 0
        for i in range(len(word)):
            if word[i] in first_map and i - first_map[word[i]] + 1 >= 4:
                res += 1
                first_map = {}
            elif word[i] not in first_map:
                first_map[word[i]] = i
        return res

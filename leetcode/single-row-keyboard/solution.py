class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        value_look = {}
        for i in range(len(keyboard)):
            value_look[keyboard[i]] = i

        last_index = 0
        res = 0
        for c in word:
            index_char = value_look[c]
            res += abs(last_index - index_char)
            last_index = index_char
        return res

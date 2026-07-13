class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split(" ")
        words_new = []
        for word in words:
            words_new.append(word[::-1])
        res = " ".join(words_new)
        return res

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        broke = set(brokenLetters)
        res = 0
        for word in text.split(" "):
            good = True
            for c in word:
                if c in broke:
                    good = False
                    break
            if good:
                res += 1
        return res

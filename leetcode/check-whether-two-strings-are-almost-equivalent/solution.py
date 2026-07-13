class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        c1 = Counter(word1)
        c2 = Counter(word2)

        for c in "qwertyuiopasdfghjklzxcvbnm":
            if abs(c1[c] - c2[c]) > 3:
                return False
        return True

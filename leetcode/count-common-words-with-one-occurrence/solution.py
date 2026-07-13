class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        c1 = Counter(words1)
        c2 = Counter(words2)
        res = 0
        for w in set(words1) | set(words2):
            if c1[w] == 1 and c2[w] == 1:
                res += 1
        return res

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        res = []
        for word in queries:
            for word2 in dictionary:
                misses = 0
                for c1, c2 in zip(word, word2):
                    if c1 != c2:
                        misses += 1
                    if misses == 3:
                        break
                if misses <= 2:
                    res.append(word)
                    break
        return res

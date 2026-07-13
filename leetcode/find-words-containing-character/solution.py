class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            word = words[i]
            for c in word:
                if c == x:
                    res.append(i)
                    break
        return res

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:

        v = set()
        word = set(words)
        for w in words:
            v.add(len(w))
        res = []
        for l in v:
            for i in range(len(text) - l + 1):
                if text[i:i+l] in words:
                    res.append([i,i+l-1])
        res.sort()
        return res

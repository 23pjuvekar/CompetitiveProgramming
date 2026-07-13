class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        c = Counter(words)
        res = 0
        for w in words:
            if w == w[::-1]:
                res -= 1
            res += c[w[::-1]]
        return res // 2

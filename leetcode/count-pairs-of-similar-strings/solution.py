class Solution:
    def similarPairs(self, words: List[str]) -> int:

        d = defaultdict(int)
        for word in words:
            d[''.join(sorted(set(word)))] += 1
        
        res = 0
        for key, val in d.items():
            res += (val * (val - 1)) // 2
        return res

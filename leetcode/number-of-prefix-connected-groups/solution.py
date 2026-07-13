class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:

        prefix_count = defaultdict(int)
        for word in words:
            if len(word) < k:
                continue
            prefix_count[word[:k]] += 1
        res = 0
        for _, amt in prefix_count.items():
            if amt > 1:
                res += 1
        return res

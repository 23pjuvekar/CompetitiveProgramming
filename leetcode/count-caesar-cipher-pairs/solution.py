class Solution:
    def countPairs(self, words: List[str]) -> int:
        signatures = defaultdict(int)
        for word in words:
            differences = tuple(
                (ord(word[index + 1]) - ord(word[index])) % 26
                for index in range(len(word) - 1)
            )
            signatures[differences] += 1
        total = 0
        for count in signatures.values():
            total += count * (count - 1) // 2
        return total

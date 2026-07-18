class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        wordSet = set(words)
        for word in words:
            for suffixStart in range(1, len(word)):
                suffix = word[suffixStart:]
                if suffix in wordSet:
                    wordSet.discard(suffix)
        return sum(len(word) + 1 for word in wordSet)

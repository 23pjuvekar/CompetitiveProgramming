class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:

        def adjacent(a, b):
            return abs(ord(a) - ord(b)) <= 1

        n = len(word)
        # First word
        keep = 0
        change = 1

        for i in range(1, n):
            next_change = min(keep, change) + 1

            if adjacent(word[i], word[i - 1]):
                next_keep = change
            else:
                next_keep = min(keep, change)
            
            keep = next_keep
            change = next_change
        
        return min(keep, change)

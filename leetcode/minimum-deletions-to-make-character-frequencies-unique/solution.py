class Solution:
    def minDeletions(self, s: str) -> int:

        counts = Counter(s)
        frequencies = list(counts.values())
        deletions = 0
        used_frequencies = set()
        frequencies.sort(reverse=True)
        for freq in frequencies:
            while freq > 0 and freq in used_frequencies:
                freq -= 1
                deletions += 1
            if freq > 0:
                used_frequencies.add(freq)
                
        return deletions

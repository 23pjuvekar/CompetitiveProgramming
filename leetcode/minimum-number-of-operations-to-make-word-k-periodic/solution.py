class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:

        n = len(word)
        segments = []
        for i in range(0, n, k):
            segments.append(word[i:i+k])
        counts = Counter(segments)
        
        max_freq = 0
        for key, val in counts.items():
            max_freq = max(max_freq, val)
        
        return (n // k) - max_freq

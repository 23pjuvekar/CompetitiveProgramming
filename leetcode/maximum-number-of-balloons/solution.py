class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        single = set("ban")
        double = set("lo")
        for c in text:
            count[c] += 1
        
        min_val = float("inf")
        for l in "ban":
            min_val = min(min_val, count[l])

        for l in "lo":
            min_val = min(min_val, count[l] // 2)
        
        return min_val

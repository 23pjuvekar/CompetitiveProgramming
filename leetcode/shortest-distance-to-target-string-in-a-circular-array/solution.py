class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:

        index = []
        n = len(words)

        for i in range(n):
            if words[i] == target:
                index.append(i)
        
        res = float("inf")
        for i in index:
            res = min(n - abs(i - startIndex), abs(i - startIndex), res)
        
        if res == float("inf"):
            return -1
        return res

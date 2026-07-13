class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        dist = float("inf")
        last_w_1 = -1
        last_w_2 = -1

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                last_w_1 = i
            
            if wordsDict[i] == word2:
                last_w_2 = i
            
            if last_w_1 != -1 and last_w_2 != -1:
                dist = min(abs(last_w_1 - last_w_2), dist)

        return dist

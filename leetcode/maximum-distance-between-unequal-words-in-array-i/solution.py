class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n = len(words)
        if words[0] != words[-1]:
            return n
        res = 0
        for i in range(n - 1):
            if words[i] != words[-1]:
                res = max(res, n - i)
                break
        for i in range(n - 1, 0, -1):
            if words[i] != words[0]:
                res = max(res, i + 1)
                break

        return res

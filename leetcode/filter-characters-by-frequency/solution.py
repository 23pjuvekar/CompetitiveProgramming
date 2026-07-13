class Solution:
    def filterCharacters(self, s: str, k: int) -> str:

        count = Counter(s)
        res = ""
        for c in s:
            if count[c] < k:
                res += c
        return res

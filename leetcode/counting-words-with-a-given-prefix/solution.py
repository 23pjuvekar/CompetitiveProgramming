class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        prefix_length = len(pref)
        res = 0
        for word in words:
            if len(word) < prefix_length:
                continue

            res += (word[:prefix_length] == pref)
        return res

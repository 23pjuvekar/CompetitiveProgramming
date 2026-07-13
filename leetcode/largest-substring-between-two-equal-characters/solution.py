class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hash_map = {}
        res = -1

        for i, c in enumerate(s):
            if c in hash_map:
                res = max(res, i - hash_map[c] - 1)
            else:
                hash_map[c] = i
            
        return res

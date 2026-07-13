# Sliding window

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        r = 0
        l = 0
        hash_map = {}
        res = 0

        while r < len(s):
            hash_map[s[r]] = 1 + hash_map.get(s[r], 0)
            while len(hash_map) == 3:
                hash_map[s[l]] -= 1
                if hash_map[s[l]] == 0:
                    del hash_map[s[l]]
                l += 1
            r += 1
            res = max(res, r - l)
            
        return res

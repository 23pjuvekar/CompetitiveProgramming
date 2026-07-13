class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        l = 0
        r = 10
        hash_map = {}
        res = []

        while r <= len(s):
            hash_map[s[l:r]] = 1 + hash_map.get(s[l:r], 0)
            if hash_map[s[l:r]] == 2:
                res.append(s[l:r])
            l += 1
            r += 1

        return res

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:

        def sv(char, limit):
            for i in "abcdefghijklmnopqrstuvwxyz":
                diff = abs(ord(char) - ord(i))
                distance = min(diff, 26 - diff)
                if distance <= limit:
                    return [i, limit - distance]
        
        res = ""
        for c in s:
            nc, k = sv(c, k)
            res += nc
        return res

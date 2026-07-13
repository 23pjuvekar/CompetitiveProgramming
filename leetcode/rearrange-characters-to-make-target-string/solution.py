class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        
        c1 = Counter(s)
        res = float("inf")
        for key, amt in Counter(target).items():
            res = min(res, c1[key] // amt)
        return res

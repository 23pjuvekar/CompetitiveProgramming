class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        
        curr = 0
        res = []
        for c in word:
            curr = (curr * 10 + int(c)) % m
            if curr % m == 0:
                res.append(1)
            else:
                res.append(0)
        return res

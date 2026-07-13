class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        c1 = Counter(deck)
        prev = -1
        for key, val in c1.items():
            if prev != -1:
                prev = gcd(val, prev)
            else:
                prev = val
        return prev > 1

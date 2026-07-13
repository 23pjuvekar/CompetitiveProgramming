class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:

        d = set(i for i in range(1, n + 1))
        
        i = 1
        c = 1
        while True:
            if i not in d:
                return list(d)
            d.remove(i)
            i += c * k
            i = i % n
            if i == 0:
                i = n
            c += 1

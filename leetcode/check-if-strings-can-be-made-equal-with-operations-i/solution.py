class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        c1o = defaultdict(int)
        c1e = defaultdict(int)
        c2o = defaultdict(int)
        c2e = defaultdict(int)
        
        for i in range(4):
            if i % 2 == 0:
                c1o[s1[i]] += 1
                c2o[s2[i]] += 1
            else:
                c1e[s1[i]] += 1
                c2e[s2[i]] += 1
        
        return c1o == c2o and c1e == c2e

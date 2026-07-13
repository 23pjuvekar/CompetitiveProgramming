class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        co = Counter(words[0])
        for w in words:
            c1 = Counter(w)
            for key, val in co.items():
                if key not in c1:
                    co[key] = 0
                if c1[key] < co[key]:
                    co[key] = c1[key]
        
        res = []
        for key, val in co.items():
            for _ in range(val):
                res.append(key)
        return res

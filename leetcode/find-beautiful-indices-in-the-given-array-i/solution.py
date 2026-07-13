class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        a_index = []
        for i in range(len(s) - len(a) + 1):
            if s[i:i+len(a)] == a:
                a_index.append(i)
        b_index = []
        for i in range(len(s) - len(b) + 1):
            if s[i:i+len(b)] == b:
                b_index.append(i)
        res = []
        for a_i in a_index:
            for b_i in b_index:
                if abs(a_i - b_i) <= k:
                    res.append(a_i)
                    break
        return res

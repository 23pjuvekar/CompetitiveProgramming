class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        ed = defaultdict(int)

        for e in edges:
            ed[e[0]] += 1
            ed[e[1]] += 2
        
        res = 0
        m = 0
        for key, val in ed.items():
            if val > m:
                res = key
                m = val
        return res

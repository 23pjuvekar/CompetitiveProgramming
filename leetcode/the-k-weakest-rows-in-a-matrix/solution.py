class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        res = []
        for i in range(len(mat)):
            res.append([sum(mat[i]), i])
        res.sort()
        
        final = []
        for r in range(k):
            final.append(res[r][1])
        return final

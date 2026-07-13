class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        for r in range(m):
            for c in range(n):
                if mat[r][c] != mat[r][(c + k) % n]:
                    return False
        return True

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        for _ in range(4):
            if mat == target:
                return True
            l = 0
            r = len(mat) - 1
            while l < r:
                mat[l], mat[r] = mat[r], mat[l]
                l += 1
                r -= 1
            
            for r in range(len(mat)):
                for c in range(r):
                    mat[r][c], mat[c][r] = mat[c][r], mat[r][c]

        
        return False

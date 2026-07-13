class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        res = [0, 0]

        for i in range(len(mat)):
            row = mat[i]
            n = sum(row)
            if n > res[1]:
                res[1] = n
                res[0] = i
        return res

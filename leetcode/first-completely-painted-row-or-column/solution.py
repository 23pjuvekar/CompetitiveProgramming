class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        R = len(mat)
        C = len(mat[0])

        rows_set = [0] * R
        cols_set = [0] * C
        hash_map = {}

        for r in range(R):
            for c in range(C):
                hash_map[mat[r][c]] = (r, c)

        for i in range(len(arr)):
            num = arr[i]
            r, c = hash_map[num]
            rows_set[r] += 1
            cols_set[c] += 1
            if rows_set[r] == C or cols_set[c] == R:
                return i

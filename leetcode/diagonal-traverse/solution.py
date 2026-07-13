class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        M = len(mat)
        N = len(mat[0])
        dictionary = defaultdict(list)
        for r in range(M):
            for c in range(N):
                dictionary[(r + c)].append(mat[r][c])
        res = []
        reverse = True
        for i in range(M + N + 1):
            if reverse:
                res.extend(dictionary[i][::-1])
                reverse = False
            else:
                res.extend(dictionary[i])
                reverse = True
        return res

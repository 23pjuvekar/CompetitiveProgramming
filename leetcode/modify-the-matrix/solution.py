class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        answer = matrix.copy()
        n = len(matrix)
        m = len(matrix[0])

        for i in range(m):
            neg_value = []
            max_val = -1
            for j in range(n):
                max_val = max(max_val, matrix[j][i])
                if matrix[j][i] == -1:
                    neg_value.append(j)
            for value in neg_value:
                answer[value][i] = max_val
        return answer

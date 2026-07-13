class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        row_p = 0
        col_p = 0
        res = [[0 for i in range(len(colSum))] for i in range(len(rowSum))]

        while row_p < len(rowSum) and col_p < len(colSum):
            min_val = min(rowSum[row_p], colSum[col_p])
            rowSum[row_p] -= min_val
            colSum[col_p] -= min_val
            res[row_p][col_p] = min_val

            if rowSum[row_p] == 0:
                row_p += 1
            if colSum[col_p] == 0:
                col_p += 1

        return res

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        start_col = 0
        end_col = len(mat[0]) - 1

        while start_col <= end_col:
            mid_col = (start_col + end_col) // 2

            max_row = 0
            for row in range(len(mat)):
                if mat[row][mid_col] > mat[max_row][mid_col]:
                    max_row = row
            
            left_val = mat[max_row][mid_col - 1] if mid_col > start_col else -1
            right_val = mat[max_row][mid_col + 1] if mid_col < end_col else -1

            if mat[max_row][mid_col] > left_val and mat[max_row][mid_col] > right_val:
                return [max_row, mid_col]
            elif mat[max_row][mid_col] > left_val:
                start_col = mid_col + 1
            else:
                end_col = mid_col - 1
        return []

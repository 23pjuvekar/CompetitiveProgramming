class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        diagnols_list = defaultdict(list)

        for r in range(len(mat)):
            for c in range(len(mat[r])):
                diagnols_list[r - c].append(mat[r][c])
        
        
        for key, value in diagnols_list.items():
            value.sort()
        
        pointers = defaultdict(int)
        for r in range(len(mat)):
            for c in range(len(mat[r])):
                mat[r][c] = diagnols_list[r - c][pointers[r - c]]
                pointers[r - c] += 1
        return mat

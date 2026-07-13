class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        arr = []
        for i in range(len(score)):
            arr.append([score[i][k], i])
        arr.sort(reverse=True)
        print(arr)
         
        res = []
        for val, row in arr:
            res.append(score[row].copy())
        return res

class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:

        A = sorted(arr)
        B = sorted(brr)
        res1 = k
        res2 = 0
        for i in range(len(A)):
            res1 += abs(A[i] - B[i])
        
        for i in range(len(arr)):
            res2 += abs(arr[i] - brr[i])

        return min(res1, res2)

class Solution:
    def trimMean(self, arr: List[int]) -> float:

        arr.sort()
        n = len(arr)
        k = n // 20
        return sum(arr[k:n-k]) / (n - 2*k)

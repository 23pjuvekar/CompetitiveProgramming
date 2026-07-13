class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse=True)
        maxA = arr[0]
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
        if arr:
            k = target / len(arr)
            lo, hi = int(k), int(k) + 1
            lo_diff = abs(sum(min(x, lo) for x in arr) - target)
            hi_diff = abs(sum(min(x, hi) for x in arr) - target)
            return lo if lo_diff <= hi_diff else hi
        return maxA

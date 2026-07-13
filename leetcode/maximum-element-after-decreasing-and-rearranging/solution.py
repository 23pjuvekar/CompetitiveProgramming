class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        res = 0
        for i in range(len(arr)):
            if arr[i] >= res + 1:
                res += 1
        return res

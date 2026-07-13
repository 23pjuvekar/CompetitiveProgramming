class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        res = []
        min_diff = float('inf')

        for index in range(1, len(arr)):
            val_1 = arr[index]
            val_2 = arr[index - 1]
            diff = abs(val_1 - val_2)

            if diff == min_diff:
                res.append([val_2, val_1])
            elif diff < min_diff:
                res = []
                min_diff = diff
                res.append([val_2, val_1])

        return res

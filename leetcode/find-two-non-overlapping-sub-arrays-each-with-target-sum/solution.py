class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        n = len(arr)
        left = [float("inf")] * n
        right = [float("inf")] * n

        l, total = 0, 0
        min_len = float("inf")
        for r in range(n):
            total += arr[r]
            while total > target:
                total -= arr[l]
                l += 1
            if total == target:
                min_len = min(min_len, r - l + 1)
            left[r] = min_len

        l, total = n - 1, 0
        min_len = float("inf")
        for r in range(n - 1, -1, -1):
            total += arr[r]
            while total > target:
                total -= arr[l]
                l -= 1
            if total == target:
                min_len = min(min_len, l - r + 1)
            right[r] = min_len

        final = float("inf")
        for i in range(n - 1):
            final = min(final, left[i] + right[i + 1])

        return final if final != float("inf") else -1

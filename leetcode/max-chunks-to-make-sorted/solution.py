class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        max_seen = -1
        res = 0
        for i in range(len(arr)):
            max_seen = max(max_seen, arr[i])
            if max_seen == i:
                res += 1
        return res

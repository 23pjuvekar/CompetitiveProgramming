from heapq import heapify, heappop
from typing import List

class Solution:
    def unmarkedSumArray(self,
                         nums: List[int],
                         queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Build a min-heap of (value, index)
        h = [(nums[i], i) for i in range(n)]
        heapify(h)

        total = sum(nums)
        seen = set()  # indices we’ve already marked
        res = []

        for idx, k in queries:
            # 1) mark the queried index if fresh
            if idx not in seen:
                seen.add(idx)
                total -= nums[idx]

            # 2) always remove k smallest *unmarked* elements
            to_remove = k
            while to_remove > 0 and h:
                val, i2 = heappop(h)
                if i2 in seen:
                    continue
                seen.add(i2)
                total -= val
                to_remove -= 1

            # 3) record the remaining sum
            res.append(total)

        return res

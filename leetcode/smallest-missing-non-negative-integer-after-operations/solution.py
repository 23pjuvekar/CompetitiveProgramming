from collections import defaultdict
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mods_map = defaultdict(int)
        for i in range(value):
            mods_map[i] = 0
        for num in nums:
            mods_map[num % value] += 1
        min_amt = float("inf")
        min_mod = -1
        for i in range(value):
            amt = mods_map[i]
            if amt < min_amt:
                min_amt = amt
                min_mod = i
        res = min_mod + min_amt * value
        return res

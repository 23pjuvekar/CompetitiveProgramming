class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:

        values = {}
        for i in range(26):
            values[chr(ord("a") + i)] = i + 1
        for cha, amt in zip(chars, vals):
            values[cha] = amt
        
        curr = 0
        res = 0
        for i in range(len(s)):
            curr += values[s[i]]
            if curr < 0:
                curr = 0
            res = max(res, curr)
        return res

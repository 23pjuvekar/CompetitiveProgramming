class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_value = {}

        for i in range(len(s)):
            last_value[s[i]] = i

        l = 0
        r = 0
        start = 0
        res = []
        while l < len(s):
            r = max(last_value[s[l]], r)
            if l == r:
                res.append(r - start + 1)
                start = l + 1
            l += 1
        return res

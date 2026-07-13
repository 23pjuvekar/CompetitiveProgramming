class Solution:
    def minChanges(self, s: str) -> int:

        last = s[0]
        curr_length = 0
        res = 0
        for c in s:
            if c == last:
                curr_length += 1
            else:
                if curr_length % 2 == 0:
                    last = c
                    curr_length = 1
                else:
                    curr_length += 1
                    res += 1
        return res

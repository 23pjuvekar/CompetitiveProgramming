class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        l = 0
        res = 0
        count = defaultdict(int)
        N = len(s)

        for r in range(len(s)):
            count[s[r]] += 1

            while len(count) == 3:
                res += (N - r)
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    count.pop(s[l])
                l += 1
        
        return res

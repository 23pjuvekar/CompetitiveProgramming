class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = 'L' + dominoes + 'R'
        res = list(s)
        prev = 0

        for i in range(1, len(s)):
            if s[i] == '.':
                continue

            if s[prev] == s[i]:
                for j in range(prev + 1, i):
                    res[j] = s[i]
            elif s[prev] == 'L' and s[i] == 'R':
                pass
            else:
                lo, hi = prev + 1, i - 1
                while lo < hi:
                    res[lo] = 'R'
                    res[hi] = 'L'
                    lo += 1
                    hi -= 1

            prev = i

        return ''.join(res[1:-1])

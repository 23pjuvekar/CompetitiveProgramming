class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        res = [1, 0]
        for i in range(len(s)):
            print(res[1])
            if widths[ord(s[i]) - ord("a")] + res[1] > 100:
                res[0] += 1
                res[1] = widths[ord(s[i]) - ord("a")] 
            elif widths[ord(s[i]) - ord("a")] + res[1] == 100:
                res[0] += 1
                res[1] = 0
            else:
                res[1] += widths[ord(s[i]) - ord("a")] 
        if res[1] == 0:
            res[0] -= 1
            res[1] = 100
        return res

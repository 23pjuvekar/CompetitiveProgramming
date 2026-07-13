class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:

        last = ''
        res = []
        last_i = 0

        for i in range(len(s)):
            c = s[i]
            if c != last:
                if i - last_i + 1 > 3:
                    res.append([last_i, i - 1])
                last = c
                last_i = i
        
        if i - last_i + 2 > 3:
            res.append([last_i, i])
                
        return res

class Solution:
    def boldWords(self, words: List[str], s: str) -> str:

        n = len(s)
        mask = [False] * n
        
        for word in words:
            m = len(word)
            for i in range(n - m + 1):
                if s[i : i + m] == word:
                    for k in range(i, i + m):
                        mask[k] = True
        
        res = []
        i = 0
        while i < n:
            if mask[i] and (i == 0 or not mask[i - 1]):
                res.append("<b>")
            
            res.append(s[i])
            
            if mask[i] and (i == n - 1 or not mask[i + 1]):
                res.append("</b>")
            i += 1
            
        return "".join(res)

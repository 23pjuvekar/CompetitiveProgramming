class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = [""]
        s = s.lower()

        for c in s:
            if c.isalpha():
                for i in range(len(res)):
                    res.append(res[i] + c.upper())
                    res[i] += c
            else:
                for i in range(len(res)):
                    res[i] += c
        return res

class Solution:
    def sortSentence(self, s: str) -> str:

        arr = s.split(" ")
        res = [""] * len(arr)
        
        for a in arr:
            res[int(a[-1]) - 1] = a[:len(a)-1]
        
        final = ""
        for r in res:
            final += r + " "
        return final[:len(final)-1]

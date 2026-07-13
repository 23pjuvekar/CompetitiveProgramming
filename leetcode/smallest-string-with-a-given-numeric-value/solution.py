class Solution:
    def getSmallestString(self, n: int, k: int) -> str:

        res = [0] * n
        k -= n
        i = -1
        while k > 0:
            val = min(25, k)
            res[i] += val 
            i -= 1
            k -= val
        
        final_string = ""
        for c in res:
            final_string += (chr(ord("a") + c))
        return final_string

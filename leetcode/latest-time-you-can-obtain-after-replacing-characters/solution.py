class Solution:
    def findLatestTime(self, s: str) -> str:
        res = ""
        if s[0] == "?" and (s[1] == "?" or s[1] == "1" or s[1] == "0"):
            res += "1"
        elif s[0] == "?":
            res += "0"
        else:
            res += s[0]
        
        if s[1] == "?" and res[0] == "0":
            res += "9"
        elif s[1] == "?" and res[0] == "1":
            res += "1"
        else:
            res += s[1]
        
        res += ":"

        if s[3] == "?":
            res += "5"
        else:
            res += s[3]
        
        if s[4] == "?":
            res += "9"
        else:
            res += s[4]
        return res

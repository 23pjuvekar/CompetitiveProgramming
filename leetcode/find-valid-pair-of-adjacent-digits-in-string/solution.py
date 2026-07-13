class Solution:
    def findValidPair(self, s: str) -> str:

        amt = Counter(s)

        for i in range(len(s) - 1):
            if (s[i] != s[i + 1]) and (amt[s[i]] == int(s[i])) and (amt[s[i+1]] == int(s[i+1])):
                return s[i:i+2]
        return ""

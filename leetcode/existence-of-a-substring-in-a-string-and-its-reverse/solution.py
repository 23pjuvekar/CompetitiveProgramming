class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        
        seen = set()

        for i in range(len(s) - 1):
            if s[i:i+2][::-1] in seen or s[i] == s[i+1]:
                return True
            seen.add(s[i:i+2])
        return False

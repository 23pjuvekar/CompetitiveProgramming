class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        i = 0
        j = 0
        n = len(str1)
        m = len(str2)

        # chr(ord("a") + ((ord(c) - ord("a") + 1) % 26))

        while i < n and j < m:
            if str1[i] == str2[j]:
                i += 1
                j += 1
            elif chr(ord("a") + ((ord(str1[i]) - ord("a") + 1) % 26)) == str2[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        return j == m

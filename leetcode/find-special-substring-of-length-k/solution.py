class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    break
                if (j - i) == k - 1:
                    if (j + 1 < len(s) and s[j + 1] == s[j]) or (i > 0 and s[i - 1] == s[i]):
                        break
                    return True
        return False

class Solution:
    def trimTrailingVowels(self, s: str) -> str:

        vowels = set("aeiou")

        i = len(s) - 1
        while i >= 0:
            if s[i] in vowels:
                i -= 1
            else:
                break
        
        
        return s[:i+1]

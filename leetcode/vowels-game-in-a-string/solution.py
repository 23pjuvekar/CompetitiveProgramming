class Solution:
    def doesAliceWin(self, s: str) -> bool:

        vowels_count = 0
        for c in s:
            if c in "aeiou":
                vowels_count += 1
        
        return vowels_count != 0

class Solution:
    def sortVowels(self, s: str) -> str:

        s = list(s)
        v = []
        vowels = set("aeiouAEIOU")

        for c in s:
            if c in vowels:
                v.append(c)
        
        v.sort()
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = v[j]
                j += 1
        return "".join(s)

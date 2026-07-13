class Solution:
    def reverseVowels(self, s: str) -> str:

        stack = []
        vowels = set("aeiouAEIOU")

        for c in s:
            if c in vowels:
                stack.append(c)
        
        res = ""
        for c in s:
            if c in vowels:
                res += stack.pop()
            else:
                res += c
        
        return res

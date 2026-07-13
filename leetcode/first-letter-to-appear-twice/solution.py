class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        appeared = set()

        for c in s:
            if c in appeared:
                return c
            appeared.add(c)

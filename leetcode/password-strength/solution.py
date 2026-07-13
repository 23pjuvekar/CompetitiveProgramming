class Solution:
    def passwordStrength(self, password: str) -> int:
        chars = set(password)
        strength = 0
        special = "!@#$"
        
        for char in chars:
            if char.islower():
                strength += 1
            elif char.isupper():
                strength += 2
            elif char.isdigit():
                strength += 3
            elif char in special:
                strength += 5
                
        return strength

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a_l = Counter(magazine)

        for c in ransomNote:
            if c not in a_l or a_l[c] == 0:
                return False
            a_l[c] -= 1
        
        return True

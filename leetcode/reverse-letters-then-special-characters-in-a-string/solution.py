class Solution:
    def reverseByType(self, s: str) -> str:
        char_indices = []
        special_indices = []
        res = [""] * len(s)
        for i in range(len(s)):
            if s[i].isalpha():
                char_indices.append(i)
            else:
                special_indices.append(i)
        
        l, r = 0, len(char_indices) - 1
        while l <= r:
            res[char_indices[l]] = s[char_indices[r]]
            res[char_indices[r]] = s[char_indices[l]]
            l += 1
            r -= 1
            
        l, r = 0, len(special_indices) - 1
        while l <= r:
            res[special_indices[l]] = s[special_indices[r]]
            res[special_indices[r]] = s[special_indices[l]]
            l += 1
            r -= 1
            
        return "".join(res)

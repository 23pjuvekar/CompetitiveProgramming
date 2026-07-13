class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_char_1 = {}
        map_char_2 = {}

        for index in range(len(s)):
            if s[index] not in map_char_1:
                map_char_1[s[index]] = t[index]
            else:
                if map_char_1[s[index]] != t[index]:
                    return False
                    
            if t[index] not in map_char_2:
                map_char_2[t[index]] = s[index]
            else:
                if map_char_2[t[index]] != s[index]:
                    return False

        return True

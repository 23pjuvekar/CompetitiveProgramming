class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        prev = 0
        res = ""
        spaces.append(len(s))
        for space in spaces:
            res += s[prev:space] + " "
            prev = space
        return res[:len(res)-1]

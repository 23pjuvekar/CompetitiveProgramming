class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res
    
    def countPali(self, string, left, right):
        res = 0
        while left >= 0 and right < len(string) and string[left] == string[right]:
            res += 1
            left -= 1
            right += 1
        return res
        
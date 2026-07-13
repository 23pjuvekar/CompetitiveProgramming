class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for l in range(len(haystack) - len(needle) + 1):
            print(1)
            if needle == haystack[l:l+len(needle)]:
                return l

        return -1

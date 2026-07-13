class Solution:
    def validPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1
        delete = 1

        while l <= r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
            
            l += 1
            r -= 1
            
        return True

    def isPalindrome(self, s: str, left: str, right: str) -> bool:
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

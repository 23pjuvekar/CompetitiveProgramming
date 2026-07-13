class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = ""
        for x in s:
            if x.isalpha() or x.isdigit():
                test += x.lower()

        l = 0
        r = len(test) - 1

        while l <= r:
            if test[l] != test[r]:
                return False
            l += 1
            r -= 1
        
        return True

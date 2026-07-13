class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        def isPalidrome(word):
            l = 0
            r = len(word) - 1
            while l <= r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True


        def halfChecker(str1, str2):
            l = 0
            r = len(str1) - 1
            while l <= r:
                if str1[l] != str2[r]:
                    return isPalidrome(str1[l:r+1]) or isPalidrome(str2[l:r+1]) 
                l += 1
                r -= 1
            return True
        
        return halfChecker(a, b) or halfChecker(b, a)

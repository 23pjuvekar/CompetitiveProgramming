class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def isPalindrome(word):
            l = 0
            r = len(word) - 1
            while l <= r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        for w in words:
            if isPalindrome(w):
                return w
        return ""

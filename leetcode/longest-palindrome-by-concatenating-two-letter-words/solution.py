class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        c = Counter(words)

        res = 0
        extra = False
        for word in words:
            if word == word[::-1]:
                if c[word] > 1:
                    res += 4
                    c[word[::-1]] -= 1
                    c[word] -= 1
                elif c[word] == 1:
                    extra = True
            else:
                if c[word[::-1]] > 0 and c[word] > 0:
                    res += 4
                    c[word[::-1]] -= 1
                    c[word] -= 1
        
        if extra:
            return res + 2
        return res

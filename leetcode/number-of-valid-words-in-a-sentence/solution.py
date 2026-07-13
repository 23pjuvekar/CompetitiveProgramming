class Solution:
    def countValidWords(self, sentence: str) -> int:
        def validWord(word):
            if not word:
                return False
            hyphen_seen = False
            for i, c in enumerate(word):
                if c.isalpha():
                    if not c.islower():
                        return False
                elif c == '-':
                    if (hyphen_seen or 
                        i == 0 or 
                        i == len(word)-1 or 
                        not (word[i-1].isalpha() and word[i+1].isalpha())):
                        return False
                    hyphen_seen = True
                elif c in '!.,':
                    if i != len(word) - 1:
                        return False
                else:
                    return False
            return True

        return sum(validWord(word) for word in sentence.split())

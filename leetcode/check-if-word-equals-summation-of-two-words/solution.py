class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        str1 = 0
        str2 = 0
        str3 = 0
        for c in firstWord:
            str1 = (ord(c) - ord("a")) + (str1 * 10)
        for c in secondWord:
            str2 = (ord(c) - ord("a")) + (str2 * 10)
        for c in targetWord:
            str3 = (ord(c) - ord("a")) + (str3 * 10)
        return str1 + str2 == str3

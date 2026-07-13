class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1, str2):
            if len(str1) > len(str2):
                return False
            n_1 = len(str1)
            n_2 = len(str2)
            return str2[:n_1] == str1 and str2[n_2 - n_1:] == str1

        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1

        return res

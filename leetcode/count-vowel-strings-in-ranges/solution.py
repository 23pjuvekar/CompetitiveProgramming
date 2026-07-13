class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        good = [0] * len(words)
        vowels = set("aeiou")
        
        for index, word in enumerate(words):
            if word[0] in vowels and word[len(word) - 1] in vowels:
                good[index] = 1
            if index != 0:
                good[index] += good[index - 1]
            
        res = []

        for querie in queries:
            first = 0
            second = 0
            if querie[0] != 0:
                first = good[querie[0] - 1]
            second = good[querie[1]]
            
            res.append(second-first)
        
        return res

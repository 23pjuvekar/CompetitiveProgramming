class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        res = []
        for word in words:
            good = True
            rules = {}
            rules2 = {}
            for x, y in zip(word, pattern):
                if (x in rules and y != rules[x]) or (y in rules2 and x != rules2[y]):
                    good = False
                    break
                else:
                    rules[x] = y
                    rules2[y] = x
            if good == True:
                res.append(word)
        return res

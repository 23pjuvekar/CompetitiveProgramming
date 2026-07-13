class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        res = set()
        for i in range(len(phrases)):
            for j in range(i + 1, len(phrases)):
                phrase_i = phrases[i].split(" ")
                phrase_j = phrases[j].split(" ")
                if phrase_i[-1] == phrase_j[0]:
                    res.add(" ".join(phrase_i + phrase_j[1:]))
                if phrase_i[0] == phrase_j[-1]:
                    res.add(" ".join(phrase_j + phrase_i[1:]))
        res = list(res)
        res.sort()
        return res

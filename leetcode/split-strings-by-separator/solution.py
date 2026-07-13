class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        res = []

        for word in words:
            arr = word.split(separator)
            for a in arr:
                if a != "":
                    res.append(a)
        return res

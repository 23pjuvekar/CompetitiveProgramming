class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        new = ""

        for c in word:
            if c.isalpha():
                if len(new) > 0 and new[-1] != " ":
                    new += " "
            else:
                new += c
        arr = new.split(" ")
        res = set()

        for a in arr:
            if a != "":
                res.add(int(a))
        return len(res)

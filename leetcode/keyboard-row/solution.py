class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        first_row = set("qwertyuiopQWERTYUIOP")
        second_row = set("asdfghjklASDFGHJKL")
        third_row = set("zxcvbnmZXCVBNM")
        res = []

        for word in words:
            first_count = 0
            second_count = 0
            third_count = 0
            for c in word:
                if c in first_row:
                    first_count += 1
                if c in second_row:
                    second_count += 1
                if c in third_row:
                    third_count += 1
            if (first_count == 0 and second_count == 0) or (first_count == 0 and third_count == 0) or (second_count == 0 and third_count == 0):
                res.append(word)

        return res

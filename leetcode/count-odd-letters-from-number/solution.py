class Solution:
    def countOddLetters(self, n: int) -> int:


        char_count = defaultdict(int)

        words = {
            "1" : "one",
            "2" : "two",
            "3" : "three",
            "4" : "four",
            "5" : "five",
            "6" : "six",
            "7" : "seven",
            "8" : "eight",
            "9" : "nine",
            "0" : "zero"
        }

        for number in str(n):
            for c in words[number]:
                char_count[c] += 1
        
        res = 0
        for key, val in char_count.items():
            if val % 2 == 1:
                res += 1

        return res

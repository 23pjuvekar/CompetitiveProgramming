class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split(" ")
        first_count = 0
        res = ""
        for i in range(len(words)):
            word = words[i]
            if i == 0:
                for c in word:
                    if c in "aeiou":
                        first_count += 1
                res += word + " "
            else:
                curr_count = 0
                for c in word:
                    if c in "aeiou":
                        curr_count += 1
                if curr_count == first_count:
                    res += word[::-1] + " "
                else:
                    res += word + " "
        return res[:len(res)-1]

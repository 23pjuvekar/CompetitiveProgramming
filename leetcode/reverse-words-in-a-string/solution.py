class Solution:
    def reverseWords(self, s: str) -> str:

        res = ""
        for item in reversed(s.split(" ")):
            if item != "":
                res += (item + " ")

        return res[:len(res)-1]

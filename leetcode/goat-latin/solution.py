class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        arr = sentence.split(" ")
        end = "a"
        res = ""
        for a in arr:
            if a[0] in "aeiouAEIOU":
                res += (a + "ma" + end + " ")
            else:
                res += (a[1:] + a[0] + "ma" + end + " ")
            end += "a"
        res = res[:len(res)-1]
        return res

class Solution:
    def reformat(self, s: str) -> str:

        digits = []
        letters = []
        for c in s:
            if c in "0123456789":
                digits.append(c)
            else:
                letters.append(c)
        if abs(len(digits) - len(letters)) > 1:
            return ""
        
        res = ""
        if len(digits) > len(letters):
            res += digits[-1]
            digits.pop()
            for i in range(len(digits)):
                res += letters[i]
                res += digits[i]
        elif len(digits) < len(letters):
            res += letters[-1]
            letters.pop()
            for i in range(len(digits)):
                res += digits[i]
                res += letters[i]
        else:
            for i in range(len(digits)):
                res += digits[i]
                res += letters[i]
        return res

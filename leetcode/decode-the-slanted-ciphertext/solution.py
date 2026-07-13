class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:

        res = ""
        cols = len(encodedText) // rows
        for i in range(cols):
            for j in range(i, len(encodedText), cols + 1):
                res += encodedText[j]
        for i in range(len(res) - 1, -1, -1):
            if res[i] != " ":
                return res[:i+1]
        return res

class Solution:
    def reorderSpaces(self, text: str) -> str:

        arr = [""]
        spaces = 0

        for c in text:
            if c == " " and arr[-1] != "":
                spaces += 1
                arr.append("")
            elif c == " ":
                spaces += 1
            else:
                arr[-1] += c
        if arr[-1] == "":
            arr.pop()
        if len(arr) - 1 != 0:
            between = spaces // (len(arr) - 1)
            end = spaces % (len(arr) - 1)
        else:
            between = 0
            end = spaces
        res = arr[0]
        for a in arr[1:]:
            for _ in range(between):
                res += " "
            res += a
        for _ in range(end):
            res += " "
        return res

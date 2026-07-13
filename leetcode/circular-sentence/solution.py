class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        arr = sentence.split(" ")
        last = arr[0][0]
        for a in arr:
            if last != a[0]:
                return False
            last = a[-1]
        return arr[0][0] == arr[-1][-1]

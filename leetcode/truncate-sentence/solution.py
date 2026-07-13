class Solution:
    def truncateSentence(self, s: str, k: int) -> str:

        arr = s.split()
        res = ""
        for i in range(k-1):
            res += arr[i] + " "
        res += arr[k-1]
        return res

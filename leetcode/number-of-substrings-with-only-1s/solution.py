class Solution:
    def numSub(self, s: str) -> int:

        arr = s.split("0")
        res = 0
        for i in range(len(arr)):
            if arr[i] != '':
                res += ((len(arr[i])) * (len(arr[i]) + 1)) // 2
        return res % ((10 ** 9) + 7)

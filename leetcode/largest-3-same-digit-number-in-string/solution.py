class Solution:
    def largestGoodInteger(self, num: str) -> str:

        res = -1
        l = 0
        r = 0
        while r < len(num):
            if r - l + 1 > 3:
                l += 1
            if num[l] != num[r]:
                l = r
            if r - l + 1 == 3:
                res = max(int(num[l]), res)
            r += 1
        if res == -1:
            return ""
        return str(res) + str(res) + str(res)

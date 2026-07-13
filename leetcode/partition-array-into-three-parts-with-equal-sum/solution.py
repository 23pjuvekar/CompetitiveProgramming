class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        total = sum(arr)
        if total % 3 != 0:
            return False
        total = total / 3
        res = [0, 0, 0]
        s = [-1, -1, -1]
        i = -1
        j = -1
        for n in arr:
            if s[0] == -1 or res[0] != total:
                res[0] += n
                s[0] = 0
            elif s[1] == -1 or res[1] != total:
                res[1] += n
                s[1] = 0
            elif s[2] == -1 or res[2] != total:
                res[2] += n
                s[2] = 0
        return res[0] == total and res[1] == total and res[2] == total and s[0] == 0 and s[1] == 0 and s[2] == 0

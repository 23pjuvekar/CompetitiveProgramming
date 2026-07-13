class Solution:
    def minOperations(self, nums: List[int]) -> int:

        c1 = Counter(nums)
        res = 0
        for k, v in c1.items():
            if v % 6 == 1:
                if v == 1:
                    return -1
                v -= 3
                res += 1
            res += ((v // 6) * 2)
            v = v % 6
            if 5 == v or v == 4:
                res += 2
            elif 3 == v or v == 2:
                res += 1
            print(res)
        return res

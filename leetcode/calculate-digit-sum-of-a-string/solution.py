class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            s_new = ""
            total = 0
            for i in range(len(s)):
                if i % k == 0 and i != 0:
                    s_new += str(total)
                    total = int(s[i])
                else:
                    total += int(s[i])
            if i == len(s) - 1:
                s_new += str(total)
            s = s_new
        return s

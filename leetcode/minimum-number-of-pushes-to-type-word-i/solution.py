class Solution:
    def minimumPushes(self, word: str) -> int:

        cnt = 1
        res = 0
        for _ in range(len(word)):
            if cnt <= 8:
                res += 1
            elif 9 <= cnt <= 16:
                res += 2
            elif cnt >= 25:
                res += 4
            else:
                res += 3
            cnt += 1
        return res

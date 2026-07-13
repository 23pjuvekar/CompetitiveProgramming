class Solution:
    def minimumOperations(self, num: str) -> int:

        n = len(num)
        res = n - num.count('0')

        for suffix in ["00", "25", "50", "75"]:
            j = 1
            deletions = 0
            for i in range(n - 1, -1, -1):
                if num[i] == suffix[j]:
                    j -= 1
                    if j < 0:
                        res = min(res, deletions)
                        break
                else:
                    deletions += 1

        return res

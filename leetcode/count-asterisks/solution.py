class Solution:
    def countAsterisks(self, s: str) -> int:

        arr = s.split("|")
        res = 0
        for i in range(len(arr)):
            if i % 2 == 0:
                for c in arr[i]:
                    if c == "*":
                        res += 1
        return res

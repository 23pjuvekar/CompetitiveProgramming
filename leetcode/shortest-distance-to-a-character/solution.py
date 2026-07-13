class Solution:
    def shortestToChar(self, s: str, char: str) -> List[int]:

        res = [0] * len(s)
        distance = float("inf")
        for i in range(len(s)):
            c = s[i]
            if c != char:
                distance += 1
            else:
                distance = 0
            res[i] = distance
        print(res)

        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c != char:
                distance += 1
            else:
                distance = 0
            res[i] = min(distance, res[i])
        print(res)
        return res

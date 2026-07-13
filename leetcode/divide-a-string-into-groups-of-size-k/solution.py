class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        res = [""]
        for c in s:
            res[-1] = res[-1] + c
            if len(res[-1]) == k:
                res.append("")
        if res[-1] == "":
            res.pop()
        for i in range(len(res[-1]), k):
            res[-1] = res[-1] + fill
        return res

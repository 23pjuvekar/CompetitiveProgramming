class Solution:
    def validStrings(self, n: int) -> List[str]:

        res = [""]

        for _ in range(n):
            for i in range(len(res)):
                if res[i] != "" and res[i][-1] == "0":
                    res[i] += "1"
                else:
                    res.append(res[i] + "0")
                    res[i] += "1"
        res.sort()
        return res

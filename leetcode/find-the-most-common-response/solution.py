class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        count = defaultdict(int)
        for r in responses:
            r = set(r)
            for c in r:
                count[c] += 1
        res = ""
        max_c = 0
        for key, val in count.items():
            if val > max_c:
                res = key
                max_c = val
            elif val == max_c:
                res = min(res, key)
        return res

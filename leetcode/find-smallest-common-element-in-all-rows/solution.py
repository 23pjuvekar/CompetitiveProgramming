class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        res = float("inf")
        n = len(mat)
        mp = defaultdict(int)
        for m in mat:
            for c in set(m):
                mp[c] += 1
                if mp[c] == n:
                    res = min(res, c)
        if res == float("inf"):
            return -1
        return res

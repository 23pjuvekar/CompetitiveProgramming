class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        cnt = 0
        c1 = Counter(arr)

        for a in arr:
            if c1[a] != 1:
                continue
            cnt += 1
            if cnt == k:
                return a
        return ""

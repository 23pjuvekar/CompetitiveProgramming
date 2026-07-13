class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        good = set()
        for i in range(n):
            good.add(i)
        for a, b in edges:
            if b in good:
                good.remove(b)
        if len(good) != 1:
            return -1
        return list(good)[0]

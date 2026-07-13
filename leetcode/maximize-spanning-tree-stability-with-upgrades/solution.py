class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        class UnionFind:
            def __init__(self, n: int):
                self.p = list(range(n))
                self.r = [0] * n

            def find(self, x: int) -> int:
                if self.p[x] != x:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

            def union(self, x: int, y: int) -> bool:
                rx, ry = self.find(x), self.find(y)
                if rx == ry:
                    return False
                if self.r[rx] < self.r[ry]:
                    self.p[rx] = ry
                elif self.r[ry] < self.r[rx]:
                    self.p[ry] = rx
                else:
                    self.p[ry] = rx
                    self.r[rx] += 1
                return True

        def can(T: int) -> bool:
            uf = UnionFind(n)
            used = 0
            for u, v, s, must in edges:
                if must == 1:
                    if s < T or not uf.union(u, v):
                        return False
                    used += 1
            need = n - 1 - used
            if need < 0:
                return False
            cost = 0
            zero, one = [], []
            for u, v, s, must in edges:
                if must == 0:
                    if s >= T:
                        zero.append((u, v))
                    elif 2 * s >= T:
                        one.append((u, v))
            for u, v in zero:
                if need == 0:
                    break
                if uf.union(u, v):
                    need -= 1
            for u, v in one:
                if need == 0:
                    break
                if uf.union(u, v):
                    cost += 1
                    if cost > k:
                        return False
                    need -= 1
            return need == 0 and cost <= k

        if not can(0):
            return -1
        lo, hi = 0, max(s for _, _, s, _ in edges) * 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

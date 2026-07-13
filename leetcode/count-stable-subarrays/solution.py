import collections

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def add(self, i, delta):
        i += 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def query_range(self, l, r):
        if l > r:
            return 0
        res = self.query(r)
        if l > 0:
            res -= self.query(l - 1)
        return res

class Solution:
    def countStableSubarrays(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        if n == 0:
            return []
        q = len(queries)

        length_of_run = [0] * n
        length_of_run[0] = 1
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                length_of_run[i] = length_of_run[i - 1] + 1
            else:
                length_of_run[i] = 1

        l_switch = [i - length_of_run[i] + 1 for i in range(n)]

        updates_by_l = collections.defaultdict(list)
        for i in range(n):
            if 0 <= l_switch[i] < n:
                updates_by_l[l_switch[i]].append(i)

        queries_by_l = collections.defaultdict(list)
        for i, (l, r) in enumerate(queries):
            queries_by_l[l].append((r, i))

        bit_j_plus_1 = FenwickTree(n)
        bit_count = FenwickTree(n)
        bit_len = FenwickTree(n)
        
        for i in range(n):
            bit_j_plus_1.add(i, i + 1)
            bit_count.add(i, 1)
            
        ans = [0] * q

        for l in range(n - 1, -1, -1):
            if l in updates_by_l:
                for j in updates_by_l[l]:
                    bit_j_plus_1.add(j, -(j + 1))
                    bit_count.add(j, -1)
                    bit_len.add(j, length_of_run[j])

            if l in queries_by_l:
                for r, query_idx in queries_by_l[l]:
                    sum_jp1_g1 = bit_j_plus_1.query_range(l, r)
                    count_g1 = bit_count.query_range(l, r)
                    ans1 = sum_jp1_g1 - l * count_g1
                    
                    ans2 = bit_len.query_range(l, r)
                    
                    ans[query_idx] = ans1 + ans2
                
        return ans

class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:

        benches = defaultdict(set)
        res = 0
        for s_id, b_id in students:
            benches[b_id].add(s_id)
            res = max(res, len(benches[b_id]))
        return res

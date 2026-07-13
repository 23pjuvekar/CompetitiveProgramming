
class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        h_diffs = set()
        h_len = len(hFences)
        for i in range(h_len):
            for j in range(i + 1, h_len):
                h_diffs.add(abs(hFences[i] - hFences[j]))
        max_side = -1
        v_len = len(vFences)
        for i in range(v_len):
            for j in range(i + 1, v_len):
                diff = abs(vFences[i] - vFences[j])
                if diff in h_diffs:
                    max_side = max(max_side, diff)
        if max_side == -1:
            return -1
        return (max_side**2) % (10**9 + 7)

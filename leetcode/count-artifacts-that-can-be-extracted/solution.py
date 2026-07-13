class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:

        dig = set((r, c) for r, c in dig)

        res = 0
        for r1, c1, r2, c2 in artifacts:
            good = True
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    if (r, c) not in dig:
                        good = False

            if good:
                res += 1

        return res

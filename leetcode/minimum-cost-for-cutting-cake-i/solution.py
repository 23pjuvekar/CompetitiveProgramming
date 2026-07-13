class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        h_p, v_p = 0, 0
        h_pieces, v_pieces = 1, 1
        res = 0
        while h_p < len(horizontalCut) and v_p < len(verticalCut):
            if horizontalCut[h_p] >= verticalCut[v_p]:
                res += horizontalCut[h_p] * v_pieces
                h_pieces += 1
                h_p += 1
            else:
                res += verticalCut[v_p] * h_pieces
                v_pieces += 1
                v_p += 1

        while h_p < len(horizontalCut):
            res += horizontalCut[h_p] * v_pieces
            h_p += 1

        while v_p < len(verticalCut):
            res += verticalCut[v_p] * h_pieces
            v_p += 1

        return res

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        neighbors = [[0, 0], [1, 0], [0, 1], [1, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
        M = len(img)
        N = len(img[0])
        res = [[0] * N for _ in range(M)]
        for r in range(M):
            for c in range(N):
                total_amt = 0
                total_sum = 0
                for nr, nc in neighbors:
                    if 0 <= nr + r < M and 0 <= nc + c < N:
                        total_amt += 1
                        total_sum += img[nr + r][nc + c]
                res[r][c] = total_sum // total_amt
        return res

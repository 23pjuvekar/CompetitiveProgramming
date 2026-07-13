class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        l = 0
        black_count = 0
        res = k

        for r in range(len(blocks)):
            if (r - l) + 1 > k:
                if blocks[l] == "B":
                    black_count -= 1
                l += 1
            if blocks[r] == "B":
                black_count += 1
            res = min(res, k - black_count)
        
        return res

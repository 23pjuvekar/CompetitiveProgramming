class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:

        max_flip = 1
        res = 0
        for i in range(len(flips)):
            flip = flips[i]
            max_flip = max(max_flip, flip)
            if max_flip == i + 1:
                res += 1
        return res

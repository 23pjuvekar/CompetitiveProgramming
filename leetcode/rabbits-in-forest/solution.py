class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        res = 0
        for key, val in Counter(answers).items():
            res += (key + 1) * ceil(val / (key + 1))
        return res

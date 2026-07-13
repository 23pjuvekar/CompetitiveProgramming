class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        

        i = 0
        res = 0
        done = set()
        while 0 <= i < len(instructions):
            if i in done:
                return res
            done.add(i)
            if instructions[i] == "add":
                res += values[i]
                i += 1
            else:
                i = i + values[i]
        return res

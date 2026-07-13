class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        states = []
        for b in bank:
            ones = 0
            for c in b:
                if c == "1":
                    ones += 1
            if ones > 0:
                states.append(ones)
        res = 0
        for i in range(len(states) - 1):
            res += states[i] * states[i+1]
        return res

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:

        res = []

        for i in range(len(currentState) - 1):
            if currentState[i:i+2] == "++":
                res.append(currentState[:i] + "--" + currentState[i+2:])
        
        return res

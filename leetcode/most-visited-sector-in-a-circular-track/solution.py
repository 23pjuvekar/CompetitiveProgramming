class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        res = []

        if rounds[0] > rounds[-1]:
            for i in range(1, rounds[-1] + 1):
                res.append(i)
            for i in range(rounds[0], n + 1):
                res.append(i)
        else:    
            for i in range(rounds[0], rounds[-1] + 1):
                res.append(i)


        return res

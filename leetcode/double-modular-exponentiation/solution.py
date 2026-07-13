class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:

        res = []
        for i in range(len(variables)):
            a, b, c, m = variables[i]
            if ( ( ( (a ** b) % (10) ) ** c ) % m ) == target:
                res.append(i)
        return res

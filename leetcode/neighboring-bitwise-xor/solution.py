class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        res = [0]

        for i in range(len(derived) - 1):
            res.append(res[-1] ^ derived[i])
        
        return res[-1] ^ res[0] == derived[-1]

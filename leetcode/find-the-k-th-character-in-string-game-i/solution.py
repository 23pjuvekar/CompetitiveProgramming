class Solution:
    def kthCharacter(self, k: int) -> str:
        
        res = "a"
        while len(res) < k:
            for i in range(len(res)):
                if res[i] == "z":
                    res += "a"
                else:
                    res += chr(ord(res[i]) + 1)
        return res[k - 1]

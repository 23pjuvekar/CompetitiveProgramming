class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        res = []
        curr = []
        key = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, string):
            if len(string) == len(digits):
                res.append(string)
                return

            for c in key[digits[i]]:
                dfs(i + 1, string + c)
            
        dfs(0, "")
        return res

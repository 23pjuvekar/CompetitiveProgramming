class Solution:
    def validDigit(self, n: int, x: int) -> bool:

        n_str = str(n)
        if n_str[0] == str(x):
            return False
        
        for c in n_str:
            if c == str(x):
                return True
        return False

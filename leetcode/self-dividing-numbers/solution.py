class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def isSelfDivide(num):
            num_string = str(num)
            for c in num_string:
                if int(c) == 0 or num % int(c) != 0:
                    return False
            return True
        
        res = []
        for num in range(left, right + 1):
            if isSelfDivide(num):
                res.append(num)
        return res

# (x c y) = x!/(x - y)!y!



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i = 0
        res = []
        while i < numRows:
            row = []
            for x in range(i+1):
                row.append(self.choose(i, x))
            res.append(row)
            i += 1
        return res

    def choose(self, number, choose):
        return int(self.factorial(number) / (self.factorial(number - choose) * self.factorial(choose)))

    def factorial(self, number):
        res = 1
        for i in range(1, number + 1):
            res *= i
        return res

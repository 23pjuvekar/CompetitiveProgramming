class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        res = 0
        for num in range(num1, num2 + 1):
            num_str = str(num)
            for i in range(1, len(num_str) - 1):
                if int(num_str[i - 1]) < int(num_str[i]) > int(num_str[i + 1]):
                    res += 1
                if int(num_str[i - 1]) > int(num_str[i]) < int(num_str[i + 1]):
                    res += 1 
        return res

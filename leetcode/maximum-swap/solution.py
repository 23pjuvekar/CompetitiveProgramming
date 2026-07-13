class Solution:
    def maximumSwap(self, num: int) -> int:

        num_string = str(num)
        res = num
        n = len(num_string)

        for i in range(n):
            for j in range(i+1, n):
                temp = num
                temp -= (int(num_string[i]) * (10**(n-i-1)))
                temp -= (int(num_string[j]) * (10**(n-j-1)))
                temp += (int(num_string[i]) * (10**(n-j-1)))
                temp += (int(num_string[j]) * (10**(n-i-1)))
                if res < temp:
                    res = temp
        return res

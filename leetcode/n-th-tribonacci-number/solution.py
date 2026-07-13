class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [0, 1, 1]
        if n < 3:
            return t[n]
        while n > 2:
            temp = t[::]
            t[2] = sum(temp)
            t[1] = temp[2]
            t[0] = temp[1]
            n -= 1
        return t[2]

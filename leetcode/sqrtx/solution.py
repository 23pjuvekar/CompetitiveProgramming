class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """


        l = 0
        r = x

        while l <= r:
            m = (l + r) // 2
            if m * m <= x < (m+1)*(m+1):
                return m
            elif x < m * m:
                r = m - 1
            else:
                l = m + 1
            
        return l

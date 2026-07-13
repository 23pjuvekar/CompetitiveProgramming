# 2 c 1 == 2!/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        res = [1]*(rowIndex+1)
        up = rowIndex
        down = 1

        for i in range(1, rowIndex):
            res[i] = res[i-1]*up/down
            up = up - 1
            down = down + 1
        return res

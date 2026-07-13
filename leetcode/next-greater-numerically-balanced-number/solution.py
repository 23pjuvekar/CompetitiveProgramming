class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        1 --> 1
        2 --> 2
        3 --> (1, 2)
        4 --> (1, 3)
        5 --> (1, 4), (2, 3)
        6 --> (1, 5), (2, 4), (1, 2, 3)
        """

        possible = [
            [[1]], 
            [[2, 2]], 
            [[1, 2, 2], [3, 3, 3]], 
            [[1, 3, 3, 3], [4, 4, 4, 4]], 
            [[1, 4, 4, 4, 4], [2, 2, 3, 3, 3], [5, 5, 5, 5, 5]],
            [[1, 5, 5, 5, 5, 5], [2, 2, 4, 4, 4, 4], [1, 2, 2, 3, 3, 3], [6, 6, 6, 6, 6, 6]],
            [[1, 2, 2, 4, 4, 4, 4]]
        ]
        self.list = []
        def generate_perms(vals, res):
            if len(vals) == 0:
                self.list.append(res)
                return
            for i in range(len(vals)):
                res_copy = res + str(vals[i])
                val_copy = vals[::]
                val_copy.remove(vals[i])
                generate_perms(val_copy, res_copy)
            



        n_len = len(str(n))
        for poss in possible[n_len-1:]:
            check_list = []
            for numbers in poss:
                generate_perms(numbers, "")
                check_list.extend(self.list)
            res = float("inf")
            for val in check_list:
                if int(val) > n:
                    res = min(int(val), res)
            if res != float("inf"):
                return res
        return -1

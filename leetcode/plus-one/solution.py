class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        num_str = ""

        for digit in digits:
            num_str += str(digit)

        num = int(num_str) + 1

        num_str_final = str(num)

        res = []
        for c in num_str_final:
            res.append(int(c))

        return res

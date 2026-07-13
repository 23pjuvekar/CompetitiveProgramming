class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        num = False
        exp = False
        sign = False
        dec = False

        for c in s:
            if c >= '0' and c <= '9':
                num = True
            elif c == 'e' or c == 'E':
                if exp or not num:
                    return False
                else:
                    exp = True
                    num = False
                    sign = False
                    dec = False
            elif c == '+' or c == '-':
                if sign or num or dec:
                    return False
                else:
                    sign = True
            elif c == '.':
                if dec or exp:
                    return False
                else:
                    dec = True
            else:
                return False
            
        return num

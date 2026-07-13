class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:

        ol = False
        ou = False
        od = False
        os = False
        n = len(password)

        if n < 8:
            return False

        for i in range(n):
            if password[i] in "abcdefghijklmnopqrstuvwxyz":
                ol = True
            elif password[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                ou = True
            elif password[i] in "0123456789":
                od = True
            elif password[i] in "!@#$%^&*()-+":
                os = True
            
        for i in range(n-1):
            if password[i] == password[i+1]:
                return False


        return ol and ou and od and os

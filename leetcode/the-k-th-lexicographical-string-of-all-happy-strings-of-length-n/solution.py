class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        perms = []

        def bt(n, string):

            if len(string) == n:
                perms.append(string)
                return

            for x in "abc":
                if len(string) > 0 and string[-1] == x:
                    continue
                bt(n, string + x)
        
        bt(n, "")
        perms.sort()
        if len(perms) < k:
            return ""
        return perms[k - 1]

class Solution:
    def capitalizeTitle(self, title: str) -> str:

        arr = title.split(" ")
        res = ""
        for a in arr:
            a = a.lower()
            if len(a) < 3:
                res += a + " "
            else:
                res += (a[0].upper() + a[1:] + " ")
        return res[:len(res)-1]

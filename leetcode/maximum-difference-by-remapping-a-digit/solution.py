class Solution:
    def minMaxDifference(self, num: int) -> int:

        mi = 0
        ma = -1
        n = str(num)

        for i in range(len(n)):
            if n[i] != "9":
                ma = i
                break
        
        ma_n = n.replace(n[ma], "9")
        mi_n = n.replace(n[mi], "0")
        print(ma_n, mi_n)
        return int(ma_n) - int(mi_n)

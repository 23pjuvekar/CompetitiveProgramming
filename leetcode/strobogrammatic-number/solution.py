class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        l = 0
        r = len(num) - 1
        bad_num = set()
        bad_num.add("2")
        bad_num.add("3")
        bad_num.add("4")
        bad_num.add("5")
        bad_num.add("7")

        while l <= r:
            if num[l] in bad_num or num[r] in bad_num:
                return False
            elif l == r and (num[l] != "8" and num[l] != "0" and num[l] != "1"):
                return False
            elif (num[l] == "6" and num[r] != "9") or (num[l] == "9" and num[r] != "6"):
                return False
            elif (num[l] == "0" and num[r] != "0") or (num[l] == "8" and num[r] != "8") or (num[l] == "1" and num[r] != "1"):
                return False
            
            l += 1
            r -= 1
        
        return True

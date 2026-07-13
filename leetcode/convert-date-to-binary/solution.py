class Solution:
    def convertDateToBinary(self, date: str) -> str:

        def toBinary(num):
            res = ""
            while num:
                res += str(num % 2)
                num = num // 2
            return res[::-1]
        
        arr = date.split("-")
        return toBinary(int(arr[0])) + "-" + toBinary(int(arr[1])) + "-" + toBinary(int(arr[2]))

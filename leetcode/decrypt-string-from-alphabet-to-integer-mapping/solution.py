class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=len(s)-1
        str1=""
        while(i>=0):
            if (s[i]=="#"):
                num=int(s[i-2:i])
                i=i-3
            else:
                num=int(s[i])
                i-=1
            str1=chr(num+96)+str1
        return str1

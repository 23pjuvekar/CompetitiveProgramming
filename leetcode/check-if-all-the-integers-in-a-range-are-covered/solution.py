class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        mx=0
        for i,j in ranges:
            if j>mx:
                mx=j
        
        arr=[0]*(mx+2)
        for i,j in ranges:
            arr[i]+=1
            arr[j+1]-=1
        l=[0]*(mx+2)
        l[0]=arr[0]
        for i in range(1,len(arr)):
            l[i]=l[i-1]+arr[i]
        if mx<right:
            return False
        for i in range(left,right+1):
            if l[i]==0:
                return False
        return True

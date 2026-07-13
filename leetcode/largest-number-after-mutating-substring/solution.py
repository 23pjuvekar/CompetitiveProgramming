class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
        started = False
        end = False
        res = ""
        for i in range(len(num)):
            if end:
                res += num[i]
            elif started:
                if int(num[i]) <= change[int(num[i])]:
                    res += str(change[int(num[i])])
                else:
                    end = True
                    res += num[i]
            else:
                if int(num[i]) < change[int(num[i])]:
                    res += str(change[int(num[i])])
                    started = True
                else:
                    res += num[i]
        return res

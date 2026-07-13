class Solution:
    def minFlips(self, target: str) -> int:

        arr = target.split("0")
        print(arr)
        cnt = 0
        for a in arr:
            if a != '':
                cnt += 1
        
        if cnt == 0:
            return 0
        elif arr[-1] != '':
            return (cnt * 2) - 1
        return cnt * 2

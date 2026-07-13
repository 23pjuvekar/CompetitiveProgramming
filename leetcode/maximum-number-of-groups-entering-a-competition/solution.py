def isPossible(grades, n, answer)->bool:
    if (answer*(answer+1))/2 <= n:
        return True 
    return False

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        low = 1 
        high = n
        while low <= high:
            mid = (low+high)//2 
            if isPossible(grades, n, mid) == False:
                high = mid - 1 
            else:
                if isPossible(grades, n , mid+1) == False:
                    return mid 
                else:
                    low = mid + 1 
        return n

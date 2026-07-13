class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        tracker = set(arr)
        curr = 1

        while k > 0:
            if curr not in tracker:
                k -= 1
            curr += 1
        
        return curr - 1

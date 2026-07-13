class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        

        for key, val in Counter(nums).items():
            if val % 2 == 1:
                return False
        
        return True

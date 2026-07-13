class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

        arr = []
        for n,i in zip(nums,index): 
            arr = arr[:i] + [n] + arr[i:]
        return arr

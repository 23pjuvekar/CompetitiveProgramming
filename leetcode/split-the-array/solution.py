class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        for key, amt in Counter(nums).items():
            if amt > 2:
                return False
        return True

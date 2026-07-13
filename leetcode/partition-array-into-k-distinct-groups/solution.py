class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:

        if len(nums) % k != 0:
            return False
        count = len(nums) // k
        for key, amt in Counter(nums).items():
            if amt > count:
                return False
        return True

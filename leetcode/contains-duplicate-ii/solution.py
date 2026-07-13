class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        tracker = set()
        l = 0

        for r in range(len(nums)):
            if nums[r] in tracker:
                return True
            tracker.add(nums[r])

            if r - l >= k:
                tracker.remove(nums[l])
                l += 1

            
        return False

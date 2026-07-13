class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:

        n = len(nums)

        def min_ops_to_target(target: int) -> int:
            ops = 0
            arr = nums[:]
            for i in range(n - 1):
                if arr[i] != target:
                    arr[i] = -arr[i]
                    arr[i+1] = -arr[i+1]
                    ops += 1
                    if ops > k:
                        return k + 1
            return ops if arr[-1] == target else k + 1
    
        return min_ops_to_target(1) <= k or min_ops_to_target(-1) <= k

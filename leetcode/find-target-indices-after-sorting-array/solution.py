class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums) - 1
        ans = set()

        nums.sort()
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans.add(mid)
                for i in range(mid + 1 , right + 1):
                    if nums[i] == target:
                        ans.add(i)
            
            if nums[mid] < target:
                if nums[left] == target:
                    ans.add(left)
                left = mid + 1
            else:
                if nums[right] == target:
                    ans.add(right)        
                right = mid - 1

        return sorted(list(ans))

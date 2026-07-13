class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def canDivide(mid):
            operations = 0
            for num in nums:
                # Calculate how many operations it would take to reduce 'num' to 'mid' or less
                if num > mid:
                    operations += (num - 1) // mid
            return operations <= maxOperations
        
        left, right = 1, max(nums)
        
        while left < right:
            mid = (left + right) // 2
            if canDivide(mid):
                right = mid  # Try to find a smaller valid bag size
            else:
                left = mid + 1  # Increase the bag size if it's too small to reduce within allowed operations
        
        return left

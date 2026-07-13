class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        total_count = Counter(nums)
        dominant_element = max(total_count, key=total_count.get)
        dominant_count = total_count[dominant_element]
        prefix_count = 0
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] == dominant_element:
                prefix_count += 1
            
            left_count = prefix_count
            right_count = dominant_count - left_count
            
            if left_count > (i + 1) // 2 and right_count > (n - (i + 1)) // 2:
                return i
        
        return -1

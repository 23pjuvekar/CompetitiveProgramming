class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(limit):
            if limit < 0:
                return 0
            left = 0
            odd_count = 0
            result = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1
                while odd_count > limit:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                result += right - left + 1
            return result
        return atMost(k) - atMost(k - 1)

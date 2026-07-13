class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0

        for group in groups:
            g_len = len(group)
            matched = False

            while i <= len(nums) - g_len:
                if nums[i:i + g_len] == group:
                    i += g_len
                    matched = True
                    break
                i += 1

            if not matched:
                return False

        return True

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            new_num = []
            mini = True
            for i in range(0, len(nums), 2):
                if mini:
                    new_num.append(min(nums[i], nums[i+1]))
                    mini = False
                else:
                    new_num.append(max(nums[i], nums[i+1]))
                    mini = True
            nums = new_num
        return nums[0]

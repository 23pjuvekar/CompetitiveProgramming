class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for index in range(len(nums)):
            value_needed = target - nums[index]
            if value_needed in hash_map:
                return [index, hash_map[value_needed]]
            hash_map[nums[index]] = index

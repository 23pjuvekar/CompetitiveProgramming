class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        nums_index = defaultdict(list)
        for i in range(len(nums)):
            nums_index[nums[i]].append(i)
        res = float("inf")
        for number, index_list in nums_index.items():
            for i in range(0, len(index_list) - 2):
                res = min(
                    res, 
                    abs(index_list[i] - index_list[i+1]) + 
                    abs(index_list[i+1] - index_list[i+2]) + 
                    abs(index_list[i] - index_list[i+2])
                )
        
        return res if res != float("inf") else -1

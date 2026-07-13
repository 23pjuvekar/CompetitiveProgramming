class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:


        num_to_values = defaultdict(list)
        for num, value in zip(nums1, nums2):
            num_to_values[num].append(value)
        elements = [[num, value] for num, value in num_to_values.items()]
        elements.sort()
        curr_total = 0
        heap = []
        mapping = {}
        for num, value_list in elements:
            mapping[num] = curr_total
            for value in value_list:
                heappush(heap, value)
                curr_total += value
            while len(heap) > k:
                removed_value = heappop(heap)
                curr_total -= removed_value
        
        res = []
        for num in nums1:
            res.append(mapping[num])
        return res

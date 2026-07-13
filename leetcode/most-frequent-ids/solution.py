class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:

        LazyHeap = []
        current_freq = defaultdict(int)
        res = []
        for num, update_amt in zip(nums, freq):
            current_freq[num] += update_amt
            heappush(LazyHeap, [-current_freq[num], num])
            while LazyHeap and -LazyHeap[0][0] != current_freq[LazyHeap[0][1]]:
                heappop(LazyHeap)
            if LazyHeap:
                res.append(-LazyHeap[0][0])
            else:
                res.append(0)
        return res

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        flipped_index_q = deque()
        res = 0
        for i in range(len(nums)):
            while flipped_index_q and flipped_index_q[0] < i:
                flipped_index_q.popleft()
            # print(flipped_index_q, res)
            if nums[i] == 0 and len(flipped_index_q) % 2 == 0:
                flipped_index = (i + k - 1)
                if flipped_index >= len(nums):
                    return -1
                flipped_index_q.append(flipped_index)
                res += 1
            elif nums[i] == 1 and len(flipped_index_q) % 2 == 1:
                flipped_index = (i + k - 1)
                if flipped_index >= len(nums):
                    return -1
                flipped_index_q.append(flipped_index)
                res += 1
        return res

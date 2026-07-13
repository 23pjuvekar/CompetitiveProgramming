class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        def get_digit_sum(n):
            return sum(int(d) for d in str(n))

        n = len(nums)
        arr = []
        for i in range(n):
            arr.append((get_digit_sum(nums[i]), nums[i], i))
        
        sorted_arr = sorted(arr)

        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or sorted_arr[i][2] == i:
                continue
            
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = sorted_arr[j][2]
                cycle_size += 1
            swaps += (cycle_size - 1)
                
        return swaps

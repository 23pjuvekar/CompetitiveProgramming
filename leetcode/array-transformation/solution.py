class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            temp_arr = list(arr) 
            has_changed = False
            for i in range(1, len(arr) - 1):
                if temp_arr[i - 1] > temp_arr[i] < temp_arr[i + 1]:
                    arr[i] += 1
                    has_changed = True
                elif temp_arr[i - 1] < temp_arr[i] > temp_arr[i + 1]:
                    arr[i] -= 1
                    has_changed = True
            if has_changed == False:
                return arr

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        length = len(arr)
        descent_index = length - 2
        while descent_index >= 0 and arr[descent_index] <= arr[descent_index + 1]:
            descent_index -= 1
        if descent_index < 0:
            return arr
        swap_index = length - 1
        while arr[swap_index] >= arr[descent_index]:
            swap_index -= 1
        while swap_index > descent_index + 1 and arr[swap_index - 1] == arr[swap_index]:
            swap_index -= 1
        arr[descent_index], arr[swap_index] = arr[swap_index], arr[descent_index]
        return arr

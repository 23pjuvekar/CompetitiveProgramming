class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        arr2_set = set(arr2)
        end = []
        for item in arr1:
            if item not in arr2_set:
                end.append(item)
        end.sort()
        amount = Counter(arr1)

        i = 0
        for num in arr2:
            for _ in range(amount[num]):
                arr1[i] = num
                i += 1
        
        for num in end:
            arr1[i] = num
            i += 1
        return arr1

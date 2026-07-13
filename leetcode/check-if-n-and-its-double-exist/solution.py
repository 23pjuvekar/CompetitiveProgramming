class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        values = set()

        for num in arr:
            if num * 2 in values or (num % 2 == 0 and num // 2 in values):
                return True
            values.add(num)
        
        return False

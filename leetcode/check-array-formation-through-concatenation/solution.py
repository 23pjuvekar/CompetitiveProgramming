class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        mapping = {}
        for piece in pieces:
            mapping[piece[0]] = piece

        res = []
        for num in arr:
            if num in mapping:
                res += mapping[num]
        return res == arr

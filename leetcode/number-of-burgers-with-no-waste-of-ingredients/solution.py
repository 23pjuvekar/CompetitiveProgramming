class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:

        if tomatoSlices % 2 == 1:
            return []
        n = tomatoSlices // 2
        m = tomatoSlices // 4
        if cheeseSlices < m or cheeseSlices > n:
            return []
        return [n - cheeseSlices, n - (n - cheeseSlices) * 2]

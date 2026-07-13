class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        n = len(candyType)
        count = Counter(candyType)
        return min(n//2,len(count))

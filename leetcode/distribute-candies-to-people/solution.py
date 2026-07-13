class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

        i = 0
        res = [0] * num_people
        while candies:
            res[i % num_people] += min(candies, i + 1)
            candies -= min(candies, i + 1)
            i += 1
        return res

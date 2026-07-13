class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:

        new = []
        vegan = []
        if veganFriendly == 0:
            vegan = [0, 1]
        else:
            vegan = [1]

        for r in restaurants:
            if r[2] in vegan and r[3] <= maxPrice and r[4] <= maxDistance:
                new.append([r[1], r[0]])
        res = []
        new.sort(reverse=True)
        for _, i in new:
            res.append(i)
        return res

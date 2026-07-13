class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = set() # Keep tracks of the indexs that are good

        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            for index, value in enumerate(trip):
                if value == target[index]:
                    good.add(index)
        
        return len(good) == 3

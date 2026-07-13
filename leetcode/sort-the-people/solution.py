class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        n = len(names)
        temp = []

        for index in range(n):
            temp.append([heights[index], names[index]])
        
        temp.sort(reverse=True)

        res = []
        for item in temp:
            res.append(item[1])

        return res

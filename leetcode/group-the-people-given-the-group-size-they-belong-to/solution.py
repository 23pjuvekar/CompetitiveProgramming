class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        groups = defaultdict(list)
        for i in range(len(groupSizes)):
            groups[groupSizes[i]].append(i)
        
        res = [[]]
        for key, val in groups.items():
            while len(val) > 0:
                res[-1].append(val[-1])
                val.pop()
                if len(res[-1]) == key:
                    res.append([])
        res.pop()
        return res

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        sets = [set(f) for f in favoriteCompanies]
        res = []
        n = len(favoriteCompanies)
        for i in range(n):
            add = 0
            for j in range(n):
                if i != j and sets[i].issubset(sets[j]):
                    add = 1
                    break
            if add == 0:
                res.append(i)

        return res

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:

        people = defaultdict(int)
        food = set()
        tables = set()
        for c, t, f in orders:
            people[(t, f)] += 1
            food.add(f)
            tables.add(t)
        food = list(food)
        food.sort()
        tables = list(tables)
        tables.sort(key=lambda x:int(x))
        res = [[]]
        res[0].append("Table")
        for f in food:
            res[0].append(f)
        for t in tables:
            res.append([t])
            for f in res[0][1:]:
                res[-1].append(str(people[(t, f)]))
        return res

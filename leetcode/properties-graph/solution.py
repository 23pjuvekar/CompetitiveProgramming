class Solution(object):
    def numberOfComponents(self, properties, k):
        n = len(properties)
        res = 0
        visit = set()
        graph = defaultdict(list)

        def intersect(a, b):
            return len(set(a) & set(b))
        
        for i in range(n):
            for j in range(i + 1, n):
                if intersect(properties[i], properties[j]) >= k:
                    graph[i].append(j)
                    graph[j].append(i)
        
        def dfs(index):
            for neighbour in graph[index]:
                if neighbour not in visit:
                    visit.add(neighbour)
                    dfs(neighbour)
        
        for i in range(n):
            if i not in visit:
                res += 1
                visit.add(i)
                dfs(i)
                
        return res

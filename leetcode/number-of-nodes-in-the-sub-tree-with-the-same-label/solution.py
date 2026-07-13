class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g, count, ans = defaultdict(list), defaultdict(int), [0] * n
        
        for a, b in edges:                            
            g[a].append(b)
            g[b].append(a)
        
        def dfs(node=0, parent=None):  
            label = labels[node]             
            cur = count[label]
            count[label] += 1            
            for child in g[node]:
                if child != parent:
                    dfs(child, node)
            ans[node] = count[label] - cur

        dfs(0, None)
        return ans

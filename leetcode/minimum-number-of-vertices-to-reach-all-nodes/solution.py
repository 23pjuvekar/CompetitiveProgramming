class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        edge_in_nodes = set()
        for _, node2 in edges:
            edge_in_nodes.add(node2)
        
        res = []
        for i in range(n):
            if i not in edge_in_nodes:
                res.append(i)
        return res

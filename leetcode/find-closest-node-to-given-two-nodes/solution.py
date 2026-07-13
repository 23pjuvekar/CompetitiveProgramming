class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def createList(node, values):
            q = deque()
            q.append(node)
            seen = set()
            dis = 0
            while q:
                n = q.popleft()
                values[n] = dis
                seen.add(n)
                if edges[n] != -1 and edges[n] not in seen:
                    q.append(edges[n])
                dis += 1
        v1 = [float("inf")] * len(edges)
        v2 = [float("inf")] * len(edges)
        createList(node1, v1)
        createList(node2, v2)
        m = float("inf")
        res = -1
        print(v1, v2)
        for i in range(len(edges)):
            x = v1[i]
            y = v2[i]
            if m > max(x, y):
                m = max(x, y)
                res = i
        return res

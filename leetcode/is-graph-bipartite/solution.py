class Solution:
    def isBipartite(self, graph):
        num_nodes = len(graph)
        color = {}
        for start_node in range(num_nodes):
            if start_node in color:
                continue
            queue = deque()
            queue.append(start_node)
            color[start_node] = 0
            while len(queue) > 0:
                current_node = queue.popleft()
                for neighbor in graph[current_node]:
                    if neighbor not in color:
                        if color[current_node] == 0:
                            color[neighbor] = 1
                        else:
                            color[neighbor] = 0
                        queue.append(neighbor)
                    elif color[neighbor] == color[current_node]:
                        return False
        return True

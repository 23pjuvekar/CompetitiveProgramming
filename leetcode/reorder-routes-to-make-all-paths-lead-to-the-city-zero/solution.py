class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjacency = defaultdict(list)
        for cityFrom, cityTo in connections:
            adjacency[cityFrom].append((cityTo, 1))
            adjacency[cityTo].append((cityFrom, 0))

        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        changesNeeded = 0

        while queue:
            currentCity = queue.popleft()
            for neighborCity, needsChange in adjacency[currentCity]:
                if visited[neighborCity] == False:
                    visited[neighborCity] = True
                    changesNeeded += needsChange
                    queue.append(neighborCity)

        return changesNeeded

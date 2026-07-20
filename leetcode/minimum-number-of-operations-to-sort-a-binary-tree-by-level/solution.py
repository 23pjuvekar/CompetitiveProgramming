class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        total_swaps = 0
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            total_swaps += self.min_swaps_to_sort(level_values)

        return total_swaps

    def min_swaps_to_sort(self, values):
        n = len(values)
        paired = []
        for i in range(n):
            paired.append((values[i], i))
        paired.sort()
        sorted_indices = []
        for value, original_index in paired:
            sorted_indices.append(original_index)

        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or sorted_indices[i] == i:
                continue
            cycle_length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = sorted_indices[j]
                cycle_length += 1
            swaps += cycle_length - 1
        return swaps

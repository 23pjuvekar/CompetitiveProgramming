class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = 0
        childrenNodes = set(leftChild + rightChild)
        for i in range(n):
            if i not in childrenNodes:
                root = i

        if sum(1 for i in range(n) if i not in childrenNodes) != 1:
            return False

        visited = set()
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)

            if leftChild[node] != -1:
                if leftChild[node] == node or leftChild[node] >= n:
                    return False
                queue.append(leftChild[node])

            if rightChild[node] != -1:
                if rightChild[node] == node or rightChild[node] >= n:
                    return False
                queue.append(rightChild[node])

        return len(visited) == n

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(c): chr(c) for c in range(ord('a'), ord('z') + 1)}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        for equation in equations:
            left, operator, right = equation[0], equation[1:3], equation[3]
            if operator == "==":
                union(left, right)

        for equation in equations:
            left, operator, right = equation[0], equation[1:3], equation[3]
            if operator == "!=":
                if find(left) == find(right):
                    return False

        return True

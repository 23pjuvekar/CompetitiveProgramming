class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        possible_set = set()
        for path in paths:
            possible_set.add(path[0])

        for path in paths:
            if path[1] not in possible_set:
                return path[1]

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        map_course = {c : [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            map_course[crs].append(pre)

        output = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for pre in map_course[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

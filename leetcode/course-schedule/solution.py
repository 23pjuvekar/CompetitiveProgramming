class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        map_course = defaultdict(list)
        for crs, pre in prerequisites:
            map_course[crs].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if map_course[course] == []:
                return True
            
            visited.add(course)
            for pre in map_course[course]:
                if dfs(pre) == False:
                    return False
            visited.remove(course)
            map_course[course] = []

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True

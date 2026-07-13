class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
        5: [1, 2, 3, 4] 5 + 7 --> 12
        4: [3] 4 + 3 --> 7
        3: [] --> 3
        2: [] --> 2
        1: [] --> 1     
        """

        def find_time(course):
            if course in memo:
                return memo[course]
            max_pre = 0
            for pre in graph[course]:
                max_pre = max(max_pre, find_time(pre))
            memo[course] = time[course - 1] + max_pre
            return memo[course]

        graph = defaultdict(list)
        memo = defaultdict(int)
        for x, y in relations:
            graph[y].append(x)
        res = 0
        for i in range(1, n + 1):
            res = max(find_time(i), res)
        return res

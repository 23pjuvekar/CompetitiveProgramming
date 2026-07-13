class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        c1 = Counter(students)
        n = len(sandwiches)

        for i in range(n):
            if c1[sandwiches[i]] == 0:
                return n - i
            c1[sandwiches[i]] -= 1
        return 0

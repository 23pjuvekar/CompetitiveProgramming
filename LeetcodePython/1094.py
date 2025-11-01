class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trip_linear = defaultdict(int)
        for people, start, end in trips:
            trip_linear[start] += people
            trip_linear[end] -= people
        trip_linear_list = [[index, people] for index, people in trip_linear.items()]
        trip_linear_list.sort()
        curr = 0
        for index, people in trip_linear_list:
            curr += people
            if curr > capacity:
                return False
        return True
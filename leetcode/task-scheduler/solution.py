class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_list = []
        counter = Counter(tasks)
        for key, value in counter.items():
            task_list.append(-value)
        heapq.heapify(task_list)
        time = 0
        q = deque()

        while task_list or q:
            time += 1
            if not task_list:
                time = q[0][0]
            else:
                item = heapq.heappop(task_list) + 1
                if item != 0:
                    q.append([time + n, item])

            if q and q[0][0] == time:
                heapq.heappush(task_list, q.popleft()[1])

        return time

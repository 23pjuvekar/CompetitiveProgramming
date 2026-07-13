class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        adj = defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                adj[m].append(i)
                
        max_time = 0
        queue = deque([(headID, 0)])
        
        while queue:
            curr_id, curr_time = queue.popleft()
            max_time = max(max_time, curr_time)
            
            for subordinate in adj[curr_id]:
                queue.append((subordinate, curr_time + informTime[curr_id]))
                
        return max_time

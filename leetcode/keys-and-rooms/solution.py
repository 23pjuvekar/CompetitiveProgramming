class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        s = set()
        q = deque()
        q.append(0)
        while q:
            n = q.popleft()
            s.add(n)
            for room in rooms[n]:
                if room not in s:
                    q.append(room)
        return len(s) == len(rooms)

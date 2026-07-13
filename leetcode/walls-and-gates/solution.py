class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # Run BFS from all gates

        ROWS = len(rooms)
        COLS = len(rooms[0])
        q = collections.deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))


        def addRoom(r, c):
            if (r not in range(ROWS)) or (c not in range(COLS)) or (rooms[r][c] == -1) or ((r, c) in visit):
                return
            visit.add((r, c))
            q.append([r, c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1

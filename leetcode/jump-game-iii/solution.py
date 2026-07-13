class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        seen = set()
        seen.add(start)
        q = deque()
        q.append(start)

        while q:
            node = q.popleft()
            if arr[node] == 0:
                return True
            if 0 <= node - arr[node] < len(arr) and node - arr[node] not in seen:
                q.append(node - arr[node])
                seen.add(node - arr[node])
            if 0 <= node + arr[node] < len(arr) and node + arr[node] not in seen:
                q.append(node + arr[node])
                seen.add(node + arr[node])

        return False

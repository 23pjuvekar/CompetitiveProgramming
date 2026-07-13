class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        if len(arr) <= k:
            return max(arr)

        q = deque(arr)
        count = 0
        curr = q.popleft()
        while count < k:
            if q[0] < curr:
                q.append(q.popleft())
                count += 1
            else:
                count = 1
                curr = q.popleft()
                q.append(curr)
        return curr

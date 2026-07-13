class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:

        order = []

        for v, l in zip(value, limit):
            order.append([l, -v])
        order.sort()
        curr = deque()
        curr_limit = 0
        res = 0
        for l, v in order:
            v = -v
            #print(v, l)
            curr_limit = l
            if len(curr) < curr_limit:
                curr.append((l, v))
                curr_limit = l
                res += v
            while curr and curr[0][0] < len(curr):
                curr.popleft()
            #print(curr, curr_limit, res)
        return res

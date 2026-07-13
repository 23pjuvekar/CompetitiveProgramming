class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:

        friends_set = set(friends)
        res = []
        for idx in order:
            if idx in friends_set:
                res.append(idx)
        return res



class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        dp_front = [0] * len(boxes)
        dp_back = [0] * len(boxes)

        carry = int(boxes[0])
        for i in range(1, len(boxes)):
            dp_front[i] = carry + dp_front[i-1]
            carry += int(boxes[i])
        
        carry = int(boxes[len(boxes)-1])
        for i in range(len(boxes)-2, -1, -1):
            dp_back[i] = carry + dp_back[i+1]
            carry += int(boxes[i])

        res = []
        for i in range(len(boxes)):
            res.append(dp_front[i] + dp_back[i])
        
        return res

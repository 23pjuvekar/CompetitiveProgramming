class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_min = (int(current[:2]) * 60) + int(current[3:])
        correct_min = (int(correct[:2]) * 60) + int(correct[3:])
        op_time = correct_min - current_min

        ops = 0
        if op_time >= 60:
            ops += op_time // 60
            op_time = op_time % 60
        
        if op_time >= 15:
            ops += op_time // 15
            op_time = op_time % 15

        if op_time >= 5:
            ops += op_time // 5
            op_time = op_time % 5

        if op_time >= 1:
            ops += op_time // 1
            op_time = op_time % 1
        
        return ops

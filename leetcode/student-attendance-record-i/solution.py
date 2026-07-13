class Solution:
    def checkRecord(self, s: str) -> bool:

        late_curr = 0
        absent_total = 0

        for c in s:
            if c == "A":
                absent_total += 1
                if absent_total == 2:
                    return False
                late_curr = 0
            elif c == "L":
                late_curr += 1
                if late_curr == 3:
                    return False
            else:
                late_curr = 0
        return True

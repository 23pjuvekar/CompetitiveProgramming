class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        left = 0
        right = 0
        under = 0

        for m in moves:
            if m == 'L':
                left += 1
            elif m == 'R':
                right += 1
            else:
                under += 1
        
        return max(left, right) + under - min(left, right)
